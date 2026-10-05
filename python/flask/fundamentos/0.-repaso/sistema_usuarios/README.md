# Sistema de Gestión de Usuarios

## Descripción

Aplicación de consola desarrollada en Python para administrar usuarios mediante inicio de sesión y control de permisos.

El sistema permite diferenciar entre usuarios ADMIN y USER.

Los administradores pueden registrar, listar, buscar, modificar y eliminar usuarios.

Los usuarios comunes solamente pueden iniciar y cerrar sesión.

## Tecnologías utilizadas

- Python
- MySQL
- PyMySQL
- Programación Orientada a Objetos

## Estructura

```text
sistema_usuarios/
│
├── main.py
├── conexion.py
├── usuario.py
├── README.md
│
├── resources/
│   ├── crear_bd.sql
│   └── poblar_datos.sql
│
└── docs/
    └── ERD.png