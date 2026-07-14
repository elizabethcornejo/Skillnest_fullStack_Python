CREATE DATABASE IF NOT EXISTS usuarios_db;
USE usuarios_db;

-- Tabla para la normalización del rol (ADMIN / USER)
CREATE TABLE IF NOT EXISTS roles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(20) NOT NULL UNIQUE
);

-- Tabla de usuarios con sus restricciones e integridad referencial
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL,
    tipo_usuario_id INT NOT NULL,
    -- Campos de auditoría (Buenas prácticas del mundo real)
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    
    FOREIGN KEY (tipo_usuario_id) REFERENCES roles(id)
);