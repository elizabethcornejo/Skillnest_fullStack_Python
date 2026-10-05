USE usuarios_db;

INSERT INTO tipos_usuario (nombre)
VALUES
('ADMIN'),
('USER');

INSERT INTO usuarios (usuario, password, tipo_usuario)
VALUES
('admin', '1234', 1),
('juan', '1234', 2),
('camila', '1234', 2);