CREATE DATABASE biblioteca;
USE biblioteca;

-- Tabla direcciones
CREATE TABLE direcciones (
    id_direccion INT PRIMARY KEY AUTO_INCREMENT,
    comuna VARCHAR(100),
    calle VARCHAR(100),
    numero_residencia VARCHAR(10),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,  -- CURRENT_TIMESTAP: valor fecha 
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    created_by INT,
    deleted TINYINT(1) DEFAULT 0
);

-- Tabla usuarios
CREATE TABLE usuarios (
    id_usuarios INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(45),
    email VARCHAR(150),
    id_direccion INT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,  -- CURRENT_TIMESTAP: valor fecha 
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    created_by INT,
    deleted TINYINT(1) DEFAULT 0,

    FOREIGN KEY (id_direccion)
    REFERENCES direcciones(id_direccion)
);

-- Tabla libros
CREATE TABLE libros (
    id_libro INT PRIMARY KEY AUTO_INCREMENT,
    autor VARCHAR(45),
    titulo VARCHAR(150),
    anio_publicacion DATETIME,
    disponible TINYINT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,  -- CURRENT_TIMESTAP: valor fecha 
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    created_by INT,
    deleted TINYINT(1) DEFAULT 0 -- Borrado logico
);

-- Tabla prestamos
CREATE TABLE prestamos (
    id_prestamo INT PRIMARY KEY AUTO_INCREMENT,
    fecha_prestamo DATETIME,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,  -- CURRENT_TIMESTAP: valor fecha 
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    created_by INT,
    deleted TINYINT(1) DEFAULT 0,
    id_usuarios INT,
    id_libro INT,

    FOREIGN KEY (id_usuarios)
    REFERENCES usuarios(id_usuarios),

    FOREIGN KEY (id_libro)
    REFERENCES libros(id_libro)
);

-- Tabla personas
CREATE TABLE personas (
    id_persona INT PRIMARY KEY AUTO_INCREMENT,
    rut VARCHAR(9),
    fecha_nac DATE,
    id_usuario INT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,  -- CURRENT_TIMESTAP: valor fecha 
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    created_by INT,
    deleted TINYINT(1) DEFAULT 0,

    FOREIGN KEY (id_usuario)
    REFERENCES usuarios(id_usuarios)
);

INSERT INTO usuarios(nombre, email)
values("Camilo", "camilo@gmailcom"),
("tete", "tete@gmail.com");


INSERT INTO personas(rut, fecha_nac, id_usuarios)
VALUES("1234567-8", "2008-06-07", 1),
("1236544-7", "2007-09-22", 2);

INSERT INTO prestamos(fecha_prestamo, id_usuarios, id_libro)
VALUES("2026-05-26", 2, 1),
("2026-07-24", 1, 2);

INSERT INTO libros(autor, titulo, anio_publicacion, disponible)
VALUES("Messi", "balon de oro", "2020-05-20", 1),
("Andres", "berlin", "2026-05-15", 0);


INSERT INTO direcciones(comuna, calle, numero_residencia)
VALUES("La Pintana", "los angeles", "1223"),
("La Granja", "dos oriente", "2465");

insert into personas(id_usuario) 
values (1),
(2);

-- Eliminación 1
select * from usuarios;

update usuarios
set deleted = 1
where id_usuarios = 1;

SELECT nombre, email
FROM usuarios
WHERE deleted = 0;

-- Eliminación 2
select * from personas;

update personas
set deleted = 1
where id_persona = 1;

select rut, fecha_nac
from personas
where deleted = 1;

-- Eliminación 3
select * from prestamos;

update prestamos
set deleted = 1
where id_prestamo = 1;

select fecha_prestamo
from prestamos
where deleted = 0; 

-- Eliminación 4
select * from libros;

update libros 
set deleted = 1
where id_libro = 1;

select autor, titulo, anio_Publicacion, disponible
from libros
where deleted = 1;

-- Eliminación 5

select * from direcciones;

update direcciones 
set deleted = 1
where id_direccion = 1;

select comuna, calle, numero_residencia
from direcciones
where deleted = 1;