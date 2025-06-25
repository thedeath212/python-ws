# Clase 2 – Programación Orientada a Objetos (POO)

## 🎯 Objetivo
Aplicar los fundamentos de la Programación Orientada a Objetos en Python creando clases, atributos y métodos que simulen el comportamiento de una tienda que gestiona productos.

---

## 📋 Instrucciones:

1. Crea un archivo con tu nombre en la carpeta 'clase2'. Ejemplo: 'nombre_apellido.py'.
2. Resuelve los ejercicios propuestos a continuación.
3. Guarda tus cambios, haz 'commit' y 'push'.
4. Crea un Pull Request a este repositorio con el título:  
   '"Clase 2 - TuNombre TuApellido"'

---

## 🧪 Ejercicio: Sistema básico de tienda

### 🛒 Descripción:
Crea una clase llamada 'Producto' y una clase 'Tienda' que permita registrar productos y simular ventas.

---

### 📌 Parte 1: Clase 'Producto'

- Atributos:
  - 'nombre' (string)
  - 'precio' (float)
  - 'stock' (entero)

- Métodos:
  - 'mostrar_info()': muestra nombre, precio y stock.
  - 'actualizar_stock(cantidad)': suma o resta stock según la cantidad (puede ser negativa).
  - 'vender(cantidad)': reduce el stock si hay suficiente, y devuelve el total a pagar. Si no hay suficiente stock, devuelve un mensaje de error.

---

### 📌 Parte 2: Clase 'Tienda'

- Atributos:
  - 'nombre' (string)
  - 'productos' (lista de objetos 'Producto')

- Métodos:
  - 'agregar_producto(producto)': añade un producto a la tienda.
  - 'listar_productos()': imprime todos los productos disponibles.
  - 'vender_producto(nombre_producto, cantidad)': busca el producto por nombre y lo vende si está disponible.

---

## ✅ Salida esperada (ejemplo):

Tienda: Super Market

Productos disponibles:

Pan | Precio: $0.50 | Stock: 20

Jugo | Precio: $1.25 | Stock: 10

Vendiendo 3 jugos...
Total a pagar: $3.75

Stock actualizado:

Jugo | Stock: 7