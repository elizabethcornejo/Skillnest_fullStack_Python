CREATE DATABASE esquema_canciones;

USE esquema_canciones;

CREATE TABLE usuarios (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(45),
    email VARCHAR(45),
    contrasena VARCHAR(45),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE canciones (
    id INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(45),
    artista VARCHAR(45),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE favoritos (
    usuario_id INT,
    cancion_id INT,
    PRIMARY KEY (usuario_id, cancion_id),
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY (cancion_id) REFERENCES canciones(id)
);