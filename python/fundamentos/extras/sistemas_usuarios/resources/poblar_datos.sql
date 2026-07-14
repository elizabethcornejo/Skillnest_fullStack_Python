USE usuarios_db;

-- Datos maestros iniciales
INSERT INTO roles (nombre) VALUES ('ADMIN'), ('USER');

-- Usuarios iniciales para pruebas del sistema
INSERT INTO usuarios (usuario, password, tipo_usuario_id) VALUES ('admin', 'admin123', 1);
INSERT INTO usuarios (usuario, password, tipo_usuario_id) VALUES ('juan', 'juan456', 2);
INSERT INTO usuarios (usuario, password, tipo_usuario_id) VALUES ('camila', 'ami789', 2);