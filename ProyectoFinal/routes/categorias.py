from flask import Blueprint, render_template, redirect, url_for, request, flash
from app import db
from models.categoria import Categoria
from flask_login import login_required

categorias_bp = Blueprint('categorias', __name__, url_prefix='/categorias')

@categorias_bp.route('/')
def listar_categorias():
    categorias = Categoria.query.all()
    return render_template('categorias/listar.html', categorias=categorias)

@categorias_bp.route('/nuevo', methods=['GET', 'POST'])
@login_required
def nuevo_categoria():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']

        if Categoria.query.filter_by(nombre=nombre).first():
            flash('Ya existe una categoría con ese nombre', 'danger')
            return redirect(url_for('categorias.nuevo_categoria'))

        categoria = Categoria(nombre=nombre, descripcion=descripcion)
        db.session.add(categoria)
        db.session.commit()
        flash('Categoría creada con éxito', 'success')
        return redirect(url_for('categorias.listar_categorias'))

    return render_template('categorias/nuevo.html')

@categorias_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def editar_categoria(id):
    categoria = Categoria.query.get_or_404(id)
    if request.method == 'POST':
        categoria.nombre = request.form['nombre']
        categoria.descripcion = request.form['descripcion']
        db.session.commit()
        flash('Categoría actualizada', 'success')
        return redirect(url_for('categorias.listar_categorias'))

    return render_template('categorias/editar.html', categoria=categoria)

@categorias_bp.route('/eliminar/<int:id>', methods=['POST'])
@login_required
def eliminar_categoria(id):
    categoria = Categoria.query.get_or_404(id)
    db.session.delete(categoria)
    db.session.commit()
    flash('Categoría eliminada', 'success')
    return redirect(url_for('categorias.listar_categorias'))
