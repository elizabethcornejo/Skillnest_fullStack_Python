CREATE DATABASE IF NOT EXISTS primera_flask;
USE primera_flask;

CREATE TABLE IF NOT EXISTS mascotas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    tipo VARCHAR(255),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

INSERT INTO mascotas (nombre, tipo) VALUES ('Fido', 'Perro');
INSERT INTO mascotas (nombre, tipo) VALUES ('Pelusa', 'Gato');
INSERT INTO mascotas (nombre, tipo) VALUES ('Max', 'Perro');