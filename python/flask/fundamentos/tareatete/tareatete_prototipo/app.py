from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    session,
    jsonify
)

from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from datetime import datetime, date, timedelta
import sqlite3


app = Flask(__name__)

app.secret_key = "schoolnest-clave-secreta-cambiar"

DATABASE = "school.db"

ROLES = [
    "estudiante",
    "profesor",
    "apoderado",
    "direccion"
]


# ============================================================
# BASE DE DATOS
# ============================================================

def get_db():

    connection = sqlite3.connect(DATABASE)

    connection.row_factory = sqlite3.Row

    return connection


def column_exists(connection, table, column):

    columns = connection.execute(
        f"PRAGMA table_info({table})"
    ).fetchall()

    return any(
        item["name"] == column
        for item in columns
    )


def migrate_database(connection):

    if not column_exists(
        connection,
        "users",
        "course"
    ):

        connection.execute(
            "ALTER TABLE users ADD COLUMN course TEXT"
        )


    if not column_exists(
        connection,
        "events",
        "audience"
    ):

        connection.execute(
            """
            ALTER TABLE events
            ADD COLUMN audience TEXT
            DEFAULT 'Todo el colegio'
            """
        )


    if not column_exists(
        connection,
        "sales",
        "status"
    ):

        connection.execute(
            """
            ALTER TABLE sales
            ADD COLUMN status TEXT
            DEFAULT 'aprobada'
            """
        )


    connection.commit()


def init_db():

    connection = get_db()

    connection.executescript(
        """

        CREATE TABLE IF NOT EXISTS users (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT NOT NULL,

            email TEXT UNIQUE NOT NULL,

            password TEXT NOT NULL,

            role TEXT NOT NULL,

            course TEXT,

            created_at TEXT DEFAULT CURRENT_TIMESTAMP

        );


        CREATE TABLE IF NOT EXISTS events (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            title TEXT NOT NULL,

            description TEXT,

            event_date TEXT NOT NULL,

            event_type TEXT DEFAULT 'evento',

            location TEXT,

            audience TEXT DEFAULT 'Todo el colegio',

            created_by INTEGER,

            created_at TEXT DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY(created_by)
            REFERENCES users(id)

        );


        CREATE TABLE IF NOT EXISTS sales (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            course TEXT NOT NULL,

            product TEXT NOT NULL,

            description TEXT,

            sale_date TEXT NOT NULL,

            price INTEGER DEFAULT 0,

            contact TEXT,

            status TEXT DEFAULT 'pendiente',

            created_by INTEGER,

            created_at TEXT DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY(created_by)
            REFERENCES users(id)

        );


        CREATE TABLE IF NOT EXISTS menus (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            menu_date TEXT UNIQUE NOT NULL,

            breakfast TEXT NOT NULL,

            lunch TEXT NOT NULL,

            notes TEXT,

            created_by INTEGER,

            created_at TEXT DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY(created_by)
            REFERENCES users(id)

        );

        """
    )

    migrate_database(connection)

    seed_demo_data(connection)

    connection.close()


def seed_demo_data(connection):

    events_count = connection.execute(
        "SELECT COUNT(*) AS total FROM events"
    ).fetchone()["total"]


    if events_count == 0:

        year = date.today().year

        demo_events = [

            (
                "Acto aniversario",
                "Celebración del aniversario de la comunidad educativa.",
                f"{year}-09-15",
                "cultural",
                "Patio central",
                "Todo el colegio"
            ),

            (
                "Reunión de apoderados",
                "Reunión general por curso.",
                f"{year}-09-22",
                "reunion",
                "Salas de clases",
                "Apoderados"
            ),

            (
                "Feria de especialidades",
                "Exposición de proyectos y especialidades.",
                f"{year}-10-08",
                "academico",
                "Gimnasio",
                "Todo el colegio"
            )

        ]

        connection.executemany(
            """

            INSERT INTO events
            (
                title,
                description,
                event_date,
                event_type,
                location,
                audience
            )

            VALUES (?, ?, ?, ?, ?, ?)

            """,
            demo_events
        )


    sales_count = connection.execute(
        "SELECT COUNT(*) AS total FROM sales"
    ).fetchone()["total"]


    if sales_count == 0:

        year = date.today().year

        demo_sales = [

            (
                "4° Medio A",
                "Brownies",
                "Venta para financiar actividades del curso.",
                f"{year}-09-11",
                1500,
                "Directiva 4°A",
                "aprobada"
            ),

            (
                "3° Medio B",
                "Completos",
                "Venta durante el segundo recreo.",
                f"{year}-09-18",
                2000,
                "Directiva 3°B",
                "aprobada"
            )

        ]

        connection.executemany(
            """

            INSERT INTO sales
            (
                course,
                product,
                description,
                sale_date,
                price,
                contact,
                status
            )

            VALUES (?, ?, ?, ?, ?, ?, ?)

            """,
            demo_sales
        )


    menus_count = connection.execute(
        "SELECT COUNT(*) AS total FROM menus"
    ).fetchone()["total"]


    if menus_count == 0:

        menus = [

            (
                "Pan con queso + leche",
                "Arroz con pollo y ensalada",
                "Incluye fruta"
            ),

            (
                "Avena con fruta",
                "Lentejas con huevo",
                "Opción vegetariana disponible"
            ),

            (
                "Pan con huevo + té",
                "Fideos con salsa boloñesa",
                "Incluye ensalada"
            ),

            (
                "Yogur + cereal",
                "Puré con hamburguesa de pavo",
                "Incluye fruta"
            ),

            (
                "Pan con palta + leche",
                "Porotos con riendas",
                "Incluye ensalada"
            )

        ]

        menu_date = date.today()

        added = 0

        while added < 5:

            if menu_date.weekday() < 5:

                breakfast, lunch, note = menus[added]

                connection.execute(
                    """

                    INSERT OR IGNORE INTO menus
                    (
                        menu_date,
                        breakfast,
                        lunch,
                        notes
                    )

                    VALUES (?, ?, ?, ?)

                    """,
                    (
                        menu_date.isoformat(),
                        breakfast,
                        lunch,
                        note
                    )
                )

                added += 1

            menu_date += timedelta(days=1)


    connection.commit()


# ============================================================
# DECORADORES
# ============================================================

def login_required(view):

    @wraps(view)

    def wrapped(*args, **kwargs):

        if "user_id" not in session:

            flash(
                "Debes iniciar sesión para continuar.",
                "warning"
            )

            return redirect(
                url_for("login")
            )

        return view(
            *args,
            **kwargs
        )

    return wrapped


def role_required(*roles):

    def decorator(view):

        @wraps(view)

        def wrapped(*args, **kwargs):

            if "user_id" not in session:

                return redirect(
                    url_for("login")
                )


            if session.get("role") not in roles:

                flash(
                    "No tienes permisos para realizar esta acción.",
                    "danger"
                )

                return redirect(
                    url_for("dashboard")
                )


            return view(
                *args,
                **kwargs
            )

        return wrapped

    return decorator


# ============================================================
# INICIO
# ============================================================

@app.route("/")
def index():

    if session.get("user_id"):

        return redirect(
            url_for("dashboard")
        )

    return render_template(
        "index.html"
    )


# ============================================================
# REGISTRO
# ============================================================

@app.route(
    "/register",
    methods=["GET", "POST"]
)
def register():

    if request.method == "POST":

        name = request.form["name"].strip()

        email = request.form["email"].strip().lower()

        password = request.form["password"]

        role = request.form["role"]

        course = request.form.get(
            "course",
            ""
        ).strip()


        if role not in ROLES:

            flash(
                "El tipo de usuario seleccionado no es válido.",
                "danger"
            )

            return redirect(
                url_for("register")
            )


        if len(password) < 6:

            flash(
                "La contraseña debe tener al menos 6 caracteres.",
                "warning"
            )

            return redirect(
                url_for("register")
            )


        connection = get_db()


        try:

            connection.execute(
                """

                INSERT INTO users
                (
                    name,
                    email,
                    password,
                    role,
                    course
                )

                VALUES (?, ?, ?, ?, ?)

                """,
                (
                    name,
                    email,
                    generate_password_hash(
                        password
                    ),
                    role,
                    course
                )
            )

            connection.commit()


        except sqlite3.IntegrityError:

            connection.close()

            flash(
                "Ese correo ya se encuentra registrado.",
                "danger"
            )

            return redirect(
                url_for("register")
            )


        connection.close()


        flash(
            "Tu cuenta fue creada correctamente.",
            "success"
        )


        return redirect(
            url_for("login")
        )


    return render_template(
        "register.html",
        roles=ROLES
    )


# ============================================================
# LOGIN
# ============================================================

@app.route(
    "/login",
    methods=["GET", "POST"]
)
def login():

    if request.method == "POST":

        email = request.form[
            "email"
        ].strip().lower()

        password = request.form[
            "password"
        ]


        connection = get_db()

        user = connection.execute(
            """

            SELECT *

            FROM users

            WHERE email = ?

            """,
            (email,)
        ).fetchone()

        connection.close()


        if not user:

            flash(
                "Correo o contraseña incorrectos.",
                "danger"
            )

            return redirect(
                url_for("login")
            )


        if not check_password_hash(
            user["password"],
            password
        ):

            flash(
                "Correo o contraseña incorrectos.",
                "danger"
            )

            return redirect(
                url_for("login")
            )


        session.clear()

        session["user_id"] = user["id"]

        session["name"] = user["name"]

        session["role"] = user["role"]

        session["course"] = user["course"] or ""


        flash(
            f"Bienvenido/a, {user['name']}.",
            "success"
        )


        return redirect(
            url_for("dashboard")
        )


    return render_template(
        "login.html"
    )


@app.route("/logout")
def logout():

    session.clear()

    return redirect(
        url_for("index")
    )


# ============================================================
# DASHBOARD
# ============================================================

@app.route("/dashboard")
@login_required
def dashboard():

    connection = get_db()

    today = date.today().isoformat()


    next_event = connection.execute(
        """

        SELECT *

        FROM events

        WHERE event_date >= ?

        ORDER BY event_date

        LIMIT 1

        """,
        (today,)
    ).fetchone()


    today_menu = connection.execute(
        """

        SELECT *

        FROM menus

        WHERE menu_date = ?

        """,
        (today,)
    ).fetchone()


    next_sale = connection.execute(
        """

        SELECT *

        FROM sales

        WHERE
            sale_date >= ?
            AND status = 'aprobada'

        ORDER BY sale_date

        LIMIT 1

        """,
        (today,)
    ).fetchone()


    upcoming_events = connection.execute(
        """

        SELECT *

        FROM events

        WHERE event_date >= ?

        ORDER BY event_date

        LIMIT 5

        """,
        (today,)
    ).fetchall()


    stats = {

        "events": connection.execute(
            """

            SELECT COUNT(*) AS total

            FROM events

            WHERE event_date >= ?

            """,
            (today,)
        ).fetchone()["total"],


        "sales": connection.execute(
            """

            SELECT COUNT(*) AS total

            FROM sales

            WHERE
                sale_date >= ?
                AND status = 'aprobada'

            """,
            (today,)
        ).fetchone()["total"],


        "menus": connection.execute(
            """

            SELECT COUNT(*) AS total

            FROM menus

            WHERE menu_date >= ?

            """,
            (today,)
        ).fetchone()["total"]

    }


    connection.close()


    return render_template(
        "dashboard.html",
        next_event=next_event,
        today_menu=today_menu,
        next_sale=next_sale,
        upcoming_events=upcoming_events,
        stats=stats
    )


# ============================================================
# CALENDARIO
# ============================================================

@app.route("/calendar")
@login_required
def calendar_view():

    return render_template(
        "calendar.html"
    )


@app.route("/api/calendar")
@login_required
def calendar_api():

    category = request.args.get(
        "category",
        "all"
    )


    connection = get_db()

    items = []


    if category in [
        "all",
        "events"
    ]:

        events = connection.execute(
            "SELECT * FROM events"
        ).fetchall()


        for event in events:

            items.append(
                {

                    "id":
                        f"event-{event['id']}",

                    "title":
                        event["title"],

                    "start":
                        event["event_date"],

                    "allDay":
                        True,

                    "backgroundColor":
                        "#2563eb",

                    "borderColor":
                        "#2563eb",

                    "extendedProps": {

                        "category":
                            "Evento escolar",

                        "description":
                            event["description"] or "",

                        "location":
                            event["location"] or "",

                        "audience":
                            event["audience"] or ""

                    }

                }
            )


    if category in [
        "all",
        "sales"
    ]:

        sales = connection.execute(
            """

            SELECT *

            FROM sales

            WHERE status = 'aprobada'

            """
        ).fetchall()


        for sale in sales:

            items.append(
                {

                    "id":
                        f"sale-{sale['id']}",

                    "title":
                        f"{sale['product']} · {sale['course']}",

                    "start":
                        sale["sale_date"],

                    "allDay":
                        True,

                    "backgroundColor":
                        "#16a34a",

                    "borderColor":
                        "#16a34a",

                    "extendedProps": {

                        "category":
                            "Venta de curso",

                        "description":
                            sale["description"] or "",

                        "location":
                            sale["contact"] or "",

                        "price":
                            sale["price"]

                    }

                }
            )


    if category in [
        "all",
        "menu"
    ]:

        menus = connection.execute(
            "SELECT * FROM menus"
        ).fetchall()


        for menu_item in menus:

            items.append(
                {

                    "id":
                        f"menu-{menu_item['id']}",

                    "title":
                        "Menú escolar",

                    "start":
                        menu_item["menu_date"],

                    "allDay":
                        True,

                    "backgroundColor":
                        "#f59e0b",

                    "borderColor":
                        "#f59e0b",

                    "extendedProps": {

                        "category":
                            "Menú escolar",

                        "description":
                            (
                                f"Desayuno: {menu_item['breakfast']} "
                                f"| Almuerzo: {menu_item['lunch']}"
                            ),

                        "location":
                            menu_item["notes"] or ""

                    }

                }
            )


    connection.close()

    return jsonify(
        items
    )


# ============================================================
# EVENTOS
# ============================================================

@app.route("/events")
@login_required
def events():

    connection = get_db()

    rows = connection.execute(
        """

        SELECT *

        FROM events

        ORDER BY event_date

        """
    ).fetchall()

    connection.close()


    return render_template(
        "events.html",
        events=rows
    )


@app.route(
    "/events/create",
    methods=["POST"]
)
@role_required(
    "direccion",
    "profesor"
)
def create_event():

    connection = get_db()

    connection.execute(
        """

        INSERT INTO events
        (
            title,
            description,
            event_date,
            event_type,
            location,
            audience,
            created_by
        )

        VALUES (?, ?, ?, ?, ?, ?, ?)

        """,
        (
            request.form["title"].strip(),

            request.form.get(
                "description",
                ""
            ).strip(),

            request.form[
                "event_date"
            ],

            request.form.get(
                "event_type",
                "evento"
            ),

            request.form.get(
                "location",
                ""
            ).strip(),

            request.form.get(
                "audience",
                "Todo el colegio"
            ).strip(),

            session[
                "user_id"
            ]
        )
    )


    connection.commit()

    connection.close()


    flash(
        "Evento publicado correctamente.",
        "success"
    )


    return redirect(
        url_for("events")
    )


@app.route(
    "/events/<int:event_id>/edit",
    methods=["POST"]
)
@role_required(
    "direccion",
    "profesor"
)
def edit_event(event_id):

    connection = get_db()

    connection.execute(
        """

        UPDATE events

        SET
            title = ?,
            description = ?,
            event_date = ?,
            event_type = ?,
            location = ?,
            audience = ?

        WHERE id = ?

        """,
        (
            request.form[
                "title"
            ].strip(),

            request.form.get(
                "description",
                ""
            ).strip(),

            request.form[
                "event_date"
            ],

            request.form.get(
                "event_type",
                "evento"
            ),

            request.form.get(
                "location",
                ""
            ).strip(),

            request.form.get(
                "audience",
                "Todo el colegio"
            ).strip(),

            event_id
        )
    )


    connection.commit()

    connection.close()


    flash(
        "Evento actualizado.",
        "success"
    )


    return redirect(
        url_for("events")
    )


@app.route(
    "/events/<int:event_id>/delete",
    methods=["POST"]
)
@role_required(
    "direccion",
    "profesor"
)
def delete_event(event_id):

    connection = get_db()

    connection.execute(
        """

        DELETE FROM events

        WHERE id = ?

        """,
        (event_id,)
    )

    connection.commit()

    connection.close()


    flash(
        "Evento eliminado.",
        "info"
    )


    return redirect(
        url_for("events")
    )


# ============================================================
# VENTAS
# ============================================================

@app.route("/sales")
@login_required
def sales():

    connection = get_db()


    if session.get("role") in [
        "direccion",
        "profesor"
    ]:

        rows = connection.execute(
            """

            SELECT *

            FROM sales

            ORDER BY sale_date

            """
        ).fetchall()


    elif session.get("role") == "estudiante":

        rows = connection.execute(
            """

            SELECT *

            FROM sales

            WHERE
                status = 'aprobada'
                OR created_by = ?

            ORDER BY sale_date

            """,
            (
                session[
                    "user_id"
                ],
            )
        ).fetchall()


    else:

        rows = connection.execute(
            """

            SELECT *

            FROM sales

            WHERE status = 'aprobada'

            ORDER BY sale_date

            """
        ).fetchall()


    connection.close()


    return render_template(
        "sales.html",
        sales=rows
    )


@app.route(
    "/sales/create",
    methods=["POST"]
)
@role_required(
    "direccion",
    "profesor",
    "estudiante"
)
def create_sale():

    if session.get("role") == "estudiante":

        status = "pendiente"

    else:

        status = "aprobada"


    connection = get_db()


    connection.execute(
        """

        INSERT INTO sales
        (
            course,
            product,
            description,
            sale_date,
            price,
            contact,
            status,
            created_by
        )

        VALUES (?, ?, ?, ?, ?, ?, ?, ?)

        """,
        (
            request.form[
                "course"
            ].strip(),

            request.form[
                "product"
            ].strip(),

            request.form.get(
                "description",
                ""
            ).strip(),

            request.form[
                "sale_date"
            ],

            int(
                request.form.get(
                    "price"
                ) or 0
            ),

            request.form.get(
                "contact",
                ""
            ).strip(),

            status,

            session[
                "user_id"
            ]
        )
    )


    connection.commit()

    connection.close()


    if status == "pendiente":

        flash(
            "La venta fue enviada para revisión.",
            "success"
        )

    else:

        flash(
            "Venta publicada correctamente.",
            "success"
        )


    return redirect(
        url_for("sales")
    )


@app.route(
    "/sales/<int:sale_id>/approve",
    methods=["POST"]
)
@role_required(
    "direccion",
    "profesor"
)
def approve_sale(sale_id):

    connection = get_db()

    connection.execute(
        """

        UPDATE sales

        SET status = 'aprobada'

        WHERE id = ?

        """,
        (sale_id,)
    )

    connection.commit()

    connection.close()


    flash(
        "Venta aprobada.",
        "success"
    )


    return redirect(
        url_for("sales")
    )


@app.route(
    "/sales/<int:sale_id>/delete",
    methods=["POST"]
)
@role_required(
    "direccion",
    "profesor"
)
def delete_sale(sale_id):

    connection = get_db()

    connection.execute(
        """

        DELETE FROM sales

        WHERE id = ?

        """,
        (sale_id,)
    )

    connection.commit()

    connection.close()


    flash(
        "Venta eliminada.",
        "info"
    )


    return redirect(
        url_for("sales")
    )


# ============================================================
# MENÚ
# ============================================================

@app.route("/menu")
@login_required
def menu():

    connection = get_db()

    rows = connection.execute(
        """

        SELECT *

        FROM menus

        ORDER BY menu_date

        """
    ).fetchall()

    connection.close()


    return render_template(
        "menu.html",
        menus=rows
    )


@app.route(
    "/menu/create",
    methods=["POST"]
)
@role_required(
    "direccion"
)
def create_menu():

    connection = get_db()

    connection.execute(
        """

        INSERT INTO menus
        (
            menu_date,
            breakfast,
            lunch,
            notes,
            created_by
        )

        VALUES (?, ?, ?, ?, ?)

        ON CONFLICT(menu_date)

        DO UPDATE SET

            breakfast =
                excluded.breakfast,

            lunch =
                excluded.lunch,

            notes =
                excluded.notes,

            created_by =
                excluded.created_by

        """,
        (
            request.form[
                "menu_date"
            ],

            request.form[
                "breakfast"
            ].strip(),

            request.form[
                "lunch"
            ].strip(),

            request.form.get(
                "notes",
                ""
            ).strip(),

            session[
                "user_id"
            ]
        )
    )


    connection.commit()

    connection.close()


    flash(
        "Menú guardado correctamente.",
        "success"
    )


    return redirect(
        url_for("menu")
    )


# ============================================================
# VARIABLES GLOBALES
# ============================================================

@app.context_processor
def global_data():

    return {

        "current_year":
            datetime.now().year

    }


# ============================================================
# EJECUTAR
# ============================================================

if __name__ == "__main__":

    init_db()

    app.run(
        debug=True
    )