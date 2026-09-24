-- 1. Crear la base de datos si no existe
CREATE DATABASE IF NOT EXISTS esquema_usuarios;

-- 2. Seleccionar la base de datos
USE esquema_usuarios;

-- 3. Crear la tabla 'usuarios'
CREATE TABLE IF NOT EXISTS usuarios (
    id INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(45) NULL,
    apellido VARCHAR(45) NULL,
    email VARCHAR(45) NULL,
    created_at DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

-- 4. Insertar datos de prueba (opcional, para ver la tabla cargada desde el inicio)
INSERT INTO usuarios (nombre, apellido, email) 
VALUES 
    ('Ricky', 'Martin', 'ricky@codingdojo.com'),
    ('Enrique', 'Iglesias', 'enrique@codingdojo.com'),
    ('Celia', 'Cruz', 'celia@codingdojo.com'),
    ('Ricardo', 'Montaner', 'ricardo@codingdojo.com');