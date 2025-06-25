# 🛒 Tarea Clase 3 – CRUD de Productos con Flask (sin Base de Datos)

## 🎯 Objetivo

Crear una aplicación web utilizando **Flask** que permita realizar operaciones básicas de un CRUD (**Crear, Leer, Actualizar, Eliminar**) sobre una lista de productos **sin usar base de datos**. La información se almacenará temporalmente en memoria usando una lista de Python.

---

## 📋 Requisitos

- Python 3.x
- Flask (instalar con `pip install flask`)
- Uso de listas para simular una base de datos

Cada producto debe tener:
- `nombre` (str)
- `precio` (float)
- `cantidad` (int)

---

## 🛠️ Funcionalidades

| Ruta | Descripción |
|------|-------------|
| `/productos` | Mostrar todos los productos |
| `/productos/nuevo` | Formulario para crear un nuevo producto |
| `/productos/editar/<id>` | Formulario para editar un producto existente |
| `/productos/eliminar/<id>` | Eliminar un producto existente |

---

## 📁 Estructura sugerida del proyecto

