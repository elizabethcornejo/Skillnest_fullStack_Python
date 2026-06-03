DROP DATABASE IF EXISTS veterinaria;

CREATE DATABASE veterinaria
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE veterinaria;
-- ==========================================
-- DIRECCIONES
-- ==========================================

CREATE TABLE direcciones (
    id_direccion INT AUTO_INCREMENT PRIMARY KEY,
    comuna VARCHAR(100) NOT NULL,
    calle VARCHAR(100) NOT NULL,
    numero_residencia VARCHAR(20) NOT NULL,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,
    created_by INT NULL,
    deleted BOOLEAN DEFAULT FALSE
);

-- ==========================================
-- DUENOS
-- ==========================================

CREATE TABLE duenos (
    id_dueno INT AUTO_INCREMENT PRIMARY KEY,

    nombre_dueno VARCHAR(100) NOT NULL,

    email VARCHAR(150) NOT NULL UNIQUE,

    telefono VARCHAR(15) NOT NULL,

    rut VARCHAR(15) NOT NULL UNIQUE,

    id_direccion INT NOT NULL,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,
    created_by INT NULL,
    deleted BOOLEAN DEFAULT FALSE,

    CONSTRAINT fk_duenos_direccion
        FOREIGN KEY (id_direccion)
        REFERENCES direcciones(id_direccion)
);

-- ==========================================
-- ESPECIES
-- ==========================================

CREATE TABLE especies (
    id_especie INT AUTO_INCREMENT PRIMARY KEY,

    nombre_especie VARCHAR(100) NOT NULL,

    descripcion_especie TEXT,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,
    created_by INT NULL,
    deleted BOOLEAN DEFAULT FALSE
);

-- ==========================================
-- RAZAS
-- ==========================================

CREATE TABLE razas (
    id_raza INT AUTO_INCREMENT PRIMARY KEY,

    nombre_raza VARCHAR(100) NOT NULL,

    descripcion_raza TEXT,

    id_especie INT NOT NULL,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,
    created_by INT NULL,
    deleted BOOLEAN DEFAULT FALSE,

    CONSTRAINT fk_raza_especie
        FOREIGN KEY (id_especie)
        REFERENCES especies(id_especie)
);

-- ==========================================
-- MASCOTAS
-- ==========================================

CREATE TABLE mascotas (
    id_mascota INT AUTO_INCREMENT PRIMARY KEY,

    nombre_mascota VARCHAR(100) NOT NULL,

    sexo_mascota ENUM('M','H') NOT NULL,

    fecha_nac DATE NOT NULL,

    peso DECIMAL(5,2) NOT NULL,

    id_dueno INT NOT NULL,

    id_especie INT NOT NULL,

    id_raza INT NOT NULL,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,
    created_by INT NULL,
    deleted BOOLEAN DEFAULT FALSE,

    CONSTRAINT fk_mascota_dueno
        FOREIGN KEY (id_dueno)
        REFERENCES duenos(id_dueno),

    CONSTRAINT fk_mascota_especie
        FOREIGN KEY (id_especie)
        REFERENCES especies(id_especie),

    CONSTRAINT fk_mascota_raza
        FOREIGN KEY (id_raza)
        REFERENCES razas(id_raza)
);

-- ==========================================
-- TIPOS DE CONSULTA
-- ==========================================

CREATE TABLE tipo_consulta (
    id_tipo_consulta INT AUTO_INCREMENT PRIMARY KEY,

    nombre_tipo_consulta VARCHAR(100) NOT NULL,

    descripcion_tipo_consulta TEXT,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,
    created_by INT NULL,
    deleted BOOLEAN DEFAULT FALSE
);

-- ==========================================
-- CONSULTAS
-- ==========================================

CREATE TABLE consultas (
    id_consulta INT AUTO_INCREMENT PRIMARY KEY,

    motivo_consulta TEXT NOT NULL,

    anamnesis TEXT NOT NULL,

    id_dueno INT NOT NULL,

    id_mascota INT NOT NULL,

    id_tipo_consulta INT NOT NULL,

    fecha_consulta DATETIME DEFAULT CURRENT_TIMESTAMP,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,
    created_by INT NULL,
    deleted BOOLEAN DEFAULT FALSE,

    CONSTRAINT fk_consulta_dueno
        FOREIGN KEY (id_dueno)
        REFERENCES duenos(id_dueno),

    CONSTRAINT fk_consulta_mascota
        FOREIGN KEY (id_mascota)
        REFERENCES mascotas(id_mascota),

    CONSTRAINT fk_consulta_tipo
        FOREIGN KEY (id_tipo_consulta)
        REFERENCES tipo_consulta(id_tipo_consulta)
);

-- ==========================================
-- TIPOS DE USUARIO
-- ==========================================

CREATE TABLE tipo_usuarios (
    id_tipo_usuario INT AUTO_INCREMENT PRIMARY KEY,

    nombre_tipo VARCHAR(50) NOT NULL,

    descripcion_tipo TEXT,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,
    created_by INT NULL,
    deleted BOOLEAN DEFAULT FALSE
);

-- ==========================================
-- USUARIOS
-- ==========================================

CREATE TABLE usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,

    username VARCHAR(50) NOT NULL UNIQUE,

    password_hash VARCHAR(255) NOT NULL,

    email VARCHAR(200) NOT NULL UNIQUE,

    id_tipo_usuario INT NOT NULL,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,
    created_by INT NULL,
    deleted BOOLEAN DEFAULT FALSE,

    CONSTRAINT fk_usuario_tipo
        FOREIGN KEY (id_tipo_usuario)
        REFERENCES tipo_usuarios(id_tipo_usuario)
);

INSERT INTO direcciones
(comuna, calle, numero_residencia)
VALUES
('Santiago','Alameda','123'),
('Providencia','Los Leones','456'),
('Nunoa','Irarrazaval','789'),
('Maipu','Pajaritos','101'),
('La Florida','Vicuna Mackenna','202'),
('Puente Alto','Concha y Toro','303'),
('Las Condes','Apoquindo','404'),
('Recoleta','Einstein','505'),
('Quilicura','San Martin','606'),
('La Reina','Larrain','707');

INSERT INTO duenos
(nombre_dueno,email,telefono,rut,id_direccion)
VALUES
('Juan Perez','juan.perez@gmail.com','+56911111111','11111111-1',1),
('Maria Gonzalez','maria.gonzalez@gmail.com','+56911111112','11111112-2',2),
('Pedro Soto','pedro.soto@gmail.com','+56911111113','11111113-3',3),
('Ana Morales','ana.morales@gmail.com','+56911111114','11111114-4',4),
('Carlos Diaz','carlos.diaz@gmail.com','+56911111115','11111115-5',5),
('Patricia Reyes','patricia.reyes@gmail.com','+56911111116','11111116-6',6),
('Jorge Fuentes','jorge.fuentes@gmail.com','+56911111117','11111117-7',7),
('Andrea Silva','andrea.silva@gmail.com','+56911111118','11111118-8',8),
('Luis Rojas','luis.rojas@gmail.com','+56911111119','11111119-9',9),
('Camila Torres','camila.torres@gmail.com','+56911111120','11111120-0',10),

('Diego Castro','diego.castro@gmail.com','+56911111121','11111121-1',1),
('Fernanda Ortiz','fernanda.ortiz@gmail.com','+56911111122','11111122-2',2),
('Ricardo Navarro','ricardo.navarro@gmail.com','+56911111123','11111123-3',3),
('Valentina Vega','valentina.vega@gmail.com','+56911111124','11111124-4',4),
('Cristian Campos','cristian.campos@gmail.com','+56911111125','11111125-5',5),
('Daniela Herrera','daniela.herrera@gmail.com','+56911111126','11111126-6',6),
('Felipe Mendez','felipe.mendez@gmail.com','+56911111127','11111127-7',7),
('Javiera Araya','javiera.araya@gmail.com','+56911111128','11111128-8',8),
('Sebastian Pino','sebastian.pino@gmail.com','+56911111129','11111129-9',9),
('Constanza Flores','constanza.flores@gmail.com','+56911111130','11111130-0',10),

('Matias Contreras','matias.contreras@gmail.com','+56911111131','11111131-1',1),
('Paula Salinas','paula.salinas@gmail.com','+56911111132','11111132-2',2),
('Rodrigo Espinoza','rodrigo.espinoza@gmail.com','+56911111133','11111133-3',3),
('Nicole Valdes','nicole.valdes@gmail.com','+56911111134','11111134-4',4),
('Ignacio Bravo','ignacio.bravo@gmail.com','+56911111135','11111135-5',5),
('Francisca Caceres','francisca.caceres@gmail.com','+56911111136','11111136-6',6),
('Martin Saavedra','martin.saavedra@gmail.com','+56911111137','11111137-7',7),
('Antonia Figueroa','antonia.figueroa@gmail.com','+56911111138','11111138-8',8),
('Benjamin Munoz','benjamin.munoz@gmail.com','+56911111139','11111139-9',9),
('Josefa Gutierrez','josefa.gutierrez@gmail.com','+56911111140','11111140-0',10);

INSERT INTO especies
(nombre_especie, descripcion_especie)
VALUES
('Perro','Caninos domesticos'),
('Gato','Felinos domesticos'),
('Conejo','Mamifero lagomorfo'),
('Ave','Aves domesticas'),
('Hamster','Roedor domestico');

INSERT INTO razas
(nombre_raza, descripcion_raza, id_especie)
VALUES
('Labrador Retriever','Perro familiar',1),
('Pastor Aleman','Perro de trabajo',1),
('Poodle','Perro pequeno',1),
('Bulldog Frances','Perro compania',1),

('Siames','Gato elegante',2),
('Persa','Gato de pelo largo',2),
('Maine Coon','Gato grande',2),

('Mini Lop','Conejo domestico',3),
('Holandes','Conejo pequeno',3),

('Canario','Ave cantora',4),
('Periquito','Ave domestica',4),

('Sirio','Hamster comun',5),
('Ruso','Hamster pequeno',5);

INSERT INTO mascotas
(nombre_mascota, sexo_mascota, fecha_nac, peso, id_dueno, id_especie, id_raza)
VALUES
('Firulais','M','2021-03-10',18.50,1,1,1),
('Luna','H','2022-01-15',4.20,2,2,5),
('Rocky','M','2020-06-22',30.00,3,1,2),
('Milo','M','2021-08-12',5.10,4,2,6),
('Nala','H','2023-02-18',3.50,5,2,5),
('Toby','M','2019-11-11',12.30,6,1,3),
('Kira','H','2020-04-05',22.10,7,1,1),
('Max','M','2022-07-14',9.80,8,1,4),
('Pelusa','H','2021-05-30',1.50,9,3,8),
('Copito','M','2022-10-09',1.80,10,3,9),

('Simba','M','2020-09-15',6.10,11,2,7),
('Mia','H','2021-12-01',4.40,12,2,6),
('Thor','M','2018-03-20',35.00,13,1,2),
('Bella','H','2022-06-10',7.20,14,1,3),
('Zeus','M','2021-07-07',28.00,15,1,1),
('Lola','H','2023-01-25',3.80,16,2,5),
('Bruno','M','2020-05-18',15.00,17,1,4),
('Moka','H','2021-11-03',4.90,18,2,7),
('Pepe','M','2022-08-12',0.90,19,4,10),
('Kiwi','H','2023-04-16',0.30,20,4,11),

('Rex','M','2019-02-14',32.00,21,1,2),
('Lucy','H','2020-10-21',6.00,22,2,6),
('Chispa','H','2021-06-08',1.20,23,3,8),
('Oreo','M','2022-03-27',2.10,24,3,9),
('Tom','M','2019-09-19',5.60,25,2,5),
('Jerry','M','2021-04-23',0.25,26,5,12),
('Nube','H','2022-12-12',0.22,27,5,13),
('Bobby','M','2020-01-30',14.50,28,1,3),
('Maggie','H','2021-08-08',19.20,29,1,1),
('Pipo','M','2023-05-05',0.35,30,4,11);

INSERT INTO tipo_consulta
(nombre_tipo_consulta, descripcion_tipo_consulta)
VALUES
('Consulta General','Revision general'),
('Vacunacion','Aplicacion de vacunas'),
('Control','Control preventivo'),
('Urgencia','Atencion de emergencia'),
('Cirugia','Procedimiento quirurgico');

INSERT INTO consultas
(motivo_consulta, anamnesis, id_dueno, id_mascota, id_tipo_consulta)
VALUES
('Vacuna anual','Mascota sana',1,1,2),
('Control peso','Sin antecedentes',2,2,3),
('Dolor estomacal','Vomitos recientes',3,3,1),
('Chequeo general','Primera visita',4,4,1),
('Vacunacion cachorro','Esquema inicial',5,5,2),
('Herida en pata','Golpe jugando',6,6,4),
('Control anual','Sin novedades',7,7,3),
('Tos persistente','Dos semanas de evolucion',8,8,1),
('Control conejo','Buen estado general',9,9,3),
('Revision dental','Mal aliento',10,10,1),

('Control felino','Sin sintomas',11,11,3),
('Vacuna triple felina','Refuerzo anual',12,12,2),
('Urgencia trauma','Accidente domestico',13,13,4),
('Chequeo general','Mascota nueva',14,14,1),
('Control cardiaco','Seguimiento',15,15,3),
('Vacuna rabia','Preventivo',16,16,2),
('Problema digestivo','Diarrea',17,17,1),
('Control general','Sin problemas',18,18,3),
('Revision ala','Ave lesionada',19,19,4),
('Chequeo ave','Preventivo',20,20,3),

('Vacuna anual','Refuerzo',21,21,2),
('Control senior','Seguimiento edad avanzada',22,22,3),
('Revision conejo','Perdida apetito',23,23,1),
('Consulta general','Primera visita',24,24,1),
('Control peso','Obesidad leve',25,25,3),
('Chequeo hamster','Normal',26,26,3),
('Revision hamster','Caida reciente',27,27,1),
('Vacunacion','Refuerzo anual',28,28,2),
('Control post tratamiento','Evolucion favorable',29,29,3),
('Consulta general','Revision inicial',30,30,1);

INSERT INTO tipo_usuarios
(nombre_tipo, descripcion_tipo)
VALUES
('Administrador','Control total del sistema'),
('Veterinario','Atencion clinica'),
('Recepcionista','Gestion de pacientes');

INSERT INTO usuarios
(username,password_hash,email,id_tipo_usuario)
VALUES
('admin','$2y$10$hash_admin','admin@veterinaria.cl',1),
('vet01','$2y$10$hash_vet01','vet01@veterinaria.cl',2),
('vet02','$2y$10$hash_vet02','vet02@veterinaria.cl',2),
('recep01','$2y$10$hash_recep01','recep01@veterinaria.cl',3),
('recep02','$2y$10$hash_recep02','recep02@veterinaria.cl',3);

show tables;
select * from usuarios;

-- Muestra la tabla mascota concatenada con otras tablas para ser mas completa 
SELECT
    m.nombre_mascota,
    d.nombre_dueno,
    e.nombre_especie
FROM mascotas m
INNER JOIN duenos d
    ON m.id_dueno = d.id_dueno
INNER JOIN especies e
    ON m.id_especie = e.id_especie;
    
SELECT
    d.nombre_dueno,
    m.nombre_mascota
FROM duenos d
INNER JOIN mascotas m
    ON d.id_dueno = m.id_dueno
WHERE d.deleted = 0
  AND m.deleted = 0
ORDER BY d.nombre_dueno ASC;
 
SELECT
    m.nombre_mascota,
    d.nombre_dueno,
    e.nombre_especie,
    r.nombre_raza,
    dir.comuna
FROM mascotas m
INNER JOIN duenos d
    ON m.id_dueno = d.id_dueno
INNER JOIN especies e
    ON m.id_especie = e.id_especie
INNER JOIN razas r
    ON m.id_raza = r.id_raza
INNER JOIN direcciones dir
    ON d.id_direccion = dir.id_direccion;
    
    SELECT
    c.id_consulta,
    c.fecha_consulta,
    m.nombre_mascota,
    d.nombre_dueno AS dueno,
    e.nombre_especie,
    r.nombre_raza,
    tc.nombre_tipo_consulta
FROM consultas c
INNER JOIN mascotas m
    ON c.id_mascota = m.id_mascota
INNER JOIN duenos d
    ON c.id_dueno = d.id_dueno
INNER JOIN especies e
    ON m.id_especie = e.id_especie
INNER JOIN razas r
    ON m.id_raza = r.id_raza
INNER JOIN tipo_consulta tc
    ON c.id_tipo_consulta = tc.id_tipo_consulta;

update duenos
set deleted = 1
where id_dueno = 23;

update duenos
set deleted = 1
where id_dueno = 6;

update duenos
set deleted = 1
where id_dueno = 19;

UPDATE direcciones
SET comuna = 'Ñuñoa',
    calle = 'Irarrázaval'
WHERE id_direccion = 3;

select * from  duenos
where deleted = 1;


show tables;