from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from models.usuario import Usuario
from flask_login import login_required, current_user

usuarios_bp = Blueprint('usuarios', __name__, url_prefix='/usuarios')

@usuarios_bp.route('/')
def listar_usuarios():

    usuarios = Usuario.query.all()
    return render_template('usuarios/listar.html', usuarios=usuarios)

@usuarios_bp.route('/nuevo', methods=['GET', 'POST'])
@login_required
def nuevo_usuario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        password = request.form['password']
        rol = request.form.get('rol', 'cliente')

        if Usuario.query.filter_by(email=email).first():
            flash('Email ya registrado.', 'danger')
            return redirect(url_for('usuarios.nuevo_usuario'))

        usuario = Usuario(nombre=nombre, email=email, rol=rol)
        usuario.set_password(password)
        db.session.add(usuario)
        db.session.commit()
        flash('Usuario creado correctamente.', 'success')
        return redirect(url_for('usuarios.listar_usuarios'))

    return render_template('usuarios/nuevo.html')

@usuarios_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def editar_usuario(id):

    usuario = Usuario.query.get_or_404(id)
    if request.method == 'POST':
        usuario.nombre = request.form['nombre']
        usuario.email = request.form['email']
        usuario.rol = request.form.get('rol', usuario.rol)
        db.session.commit()
        flash('Usuario actualizado.', 'success')
        return redirect(url_for('usuarios.listar_usuarios'))

    return render_template('usuarios/editar.html', usuario=usuario)

@usuarios_bp.route('/eliminar/<int:id>', methods=['POST'])
@login_required
def eliminar_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    flash('Usuario eliminado.', 'success')
    return redirect(url_for('usuarios.listar_usuarios'))
