CREATE DATABASE IF NOT EXISTS primera_flask;
USE primera_flask;

CREATE TABLE IF NOT EXISTS mascotas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    tipo VARCHAR(255),
    color VARCHAR(255),
    created_at DATETIME DEFAULT NOW(),
    updated_at DATETIME DEFAULT NOW()
);