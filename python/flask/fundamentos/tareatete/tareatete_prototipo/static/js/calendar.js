document.addEventListener(
    "DOMContentLoaded",
    function () {


        const calendarElement =
            document.getElementById(
                "calendar"
            );


        if (
            !calendarElement
        ) {

            return;

        }


        let activeCategory =
            "all";


        const title =
            document.getElementById(
                "detailTitle"
            );

        const description =
            document.getElementById(
                "detailDescription"
            );

        const metadata =
            document.getElementById(
                "detailMeta"
            );



        const calendar =
            new FullCalendar.Calendar(
                calendarElement,
                {

                    initialView:
                        "dayGridMonth",

                    locale:
                        "es",

                    firstDay:
                        1,

                    height:
                        "auto",

                    dayMaxEvents:
                        true,


                    headerToolbar: {

                        left:
                            "prev,next today",

                        center:
                            "title",

                        right:
                            "dayGridMonth,listMonth"

                    },


                    buttonText: {

                        today:
                            "Hoy",

                        month:
                            "Mes",

                        list:
                            "Lista"

                    },


                    events:
                        function (
                            info,
                            successCallback,
                            failureCallback
                        ) {

                            fetch(
                                `/api/calendar?category=${activeCategory}`
                            )

                                .then(
                                    response =>
                                        response.json()
                                )

                                .then(
                                    data => {

                                        successCallback(
                                            data
                                        );

                                    }
                                )

                                .catch(
                                    error => {

                                        console.error(
                                            error
                                        );

                                        failureCallback(
                                            error
                                        );

                                    }
                                );

                        },


                    eventClick:
                        function (info) {


                            const props =
                                info.event
                                    .extendedProps;


                            title.textContent =
                                info.event.title;


                            description.textContent =
                                props.description ||
                                "Sin descripción.";


                            let html = `

                                <span class="detail-category">

                                    ${props.category || "Actividad"}

                                </span>

                            `;


                            html += `

                                <div class="detail-row">

                                    <span>

                                        Fecha

                                    </span>

                                    <strong>

                                        ${info.event.startStr}

                                    </strong>

                                </div>

                            `;


                            if (
                                props.location
                            ) {

                                html += `

                                    <div class="detail-row">

                                        <span>

                                            Información

                                        </span>

                                        <strong>

                                            ${props.location}

                                        </strong>

                                    </div>

                                `;

                            }


                            if (
                                props.audience
                            ) {

                                html += `

                                    <div class="detail-row">

                                        <span>

                                            Público

                                        </span>

                                        <strong>

                                            ${props.audience}

                                        </strong>

                                    </div>

                                `;

                            }


                            if (
                                props.price !==
                                undefined
                            ) {

                                html += `

                                    <div class="detail-row">

                                        <span>

                                            Precio

                                        </span>

                                        <strong>

                                            $${Number(
                                                props.price
                                            ).toLocaleString(
                                                "es-CL"
                                            )}

                                        </strong>

                                    </div>

                                `;

                            }


                            metadata.innerHTML =
                                html;

                        }

                }
            );


        calendar.render();



        document
            .querySelectorAll(
                "[data-calendar-filter]"
            )
            .forEach(
                function (button) {

                    button.addEventListener(
                        "click",
                        function () {


                            document
                                .querySelectorAll(
                                    "[data-calendar-filter]"
                                )
                                .forEach(
                                    function (
                                        item
                                    ) {

                                        item.classList.remove(
                                            "active"
                                        );

                                    }
                                );


                            button.classList.add(
                                "active"
                            );


                            activeCategory =
                                button.dataset
                                    .calendarFilter;


                            calendar.refetchEvents();

                        }
                    );

                }
            );


    }
);