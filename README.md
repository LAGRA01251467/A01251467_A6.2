# Sistema de Reservación de Hoteles

Este proyecto es una aplicación de consola en Python para gestionar hoteles, clientes y reservaciones, utilizando archivos JSON para la persistencia de datos. Diseñado bajo estándares de calidad de software (PEP8), pruebas unitarias y análisis estático.

## Características
- **Gestión de Hoteles:** Crear, borrar, modificar y mostrar hoteles.
- **Gestión de Clientes:** Administración de perfiles de usuario.
- **Gestión de Reservas:** Control de reservaciones vinculando clientes y hoteles.
- **Persistencia:** Almacenamiento automático en archivos `.json`.

## Herramientas de Calidad
El proyecto cumple con los siguientes estándares:
- **Pylint:** Puntuación de 10/10.
- **Flake8:** Cumplimiento total de PEP8.
- **Coverage:** Cobertura de pruebas unitarias del 97%.

## Requisitos
- Python 3.x
- Librerías: `pylint`, `flake8`, `coverage`

## Ejecución de Pruebas
Para correr las pruebas unitarias y generar el reporte de cobertura, utiliza:
```bash
coverage run -m unittest discover
coverage report -m
flake8 *.py
pylint *.py
