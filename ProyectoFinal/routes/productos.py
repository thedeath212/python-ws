from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from app import db
from models.producto import Producto
from models.categoria import Categoria
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
import os

productos_bp = Blueprint('productos', __name__, url_prefix='/productos')

@productos_bp.route('/')
def listar_productos():
    productos = Producto.query.all()
    return render_template('productos/listar.html', productos=productos)

@productos_bp.route('/nuevo', methods=['GET', 'POST'])
@login_required
def nuevo_producto():
    categorias = Categoria.query.all()
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        precio = float(request.form['precio'])
        cantidad = int(request.form['cantidad'])
        categoria_id = int(request.form['categoria_id'])

        imagen = None
        if 'imagen' in request.files:
            file = request.files['imagen']
            if file.filename != '':
                filename = secure_filename(file.filename)
                ruta_guardado = os.path.join(current_app.root_path, 'static/uploads', filename)
                file.save(ruta_guardado)
                imagen = 'uploads/' + filename

        producto = Producto(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            cantidad=cantidad,
            categoria_id=categoria_id,
            imagen=imagen
        )

        db.session.add(producto)
        db.session.commit()
        flash('Producto creado correctamente.', 'success')
        return redirect(url_for('productos.listar_productos'))

    return render_template('productos/nuevo.html', categorias=categorias)

@productos_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def editar_producto(id):
    producto = Producto.query.get_or_404(id)
    categorias = Categoria.query.all()
    if request.method == 'POST':
        producto.nombre = request.form['nombre']
        producto.descripcion = request.form['descripcion']
        producto.precio = float(request.form['precio'])
        producto.cantidad = int(request.form['cantidad'])
        producto.categoria_id = int(request.form['categoria_id'])

        if 'imagen' in request.files:
            file = request.files['imagen']
            if file.filename != '':
                filename = secure_filename(file.filename)
                ruta_guardado = os.path.join(current_app.root_path, 'static/uploads', filename)
                file.save(ruta_guardado)
                producto.imagen = 'uploads/' + filename

        db.session.commit()
        flash('Producto actualizado.', 'success')
        return redirect(url_for('productos.listar_productos'))

    return render_template('productos/editar.html', producto=producto, categorias=categorias)

@productos_bp.route('/eliminar/<int:id>', methods=['POST'])
@login_required
def eliminar_producto(id):
    
    producto = Producto.query.get_or_404(id)
    db.session.delete(producto)
    db.session.commit()
    flash('Producto eliminado.', 'success')
    return redirect(url_for('productos.listar_productos'))
