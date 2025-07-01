from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from models.usuario import Usuario

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('categorias.listar_categorias'))

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = Usuario.query.filter_by(email=email).first()

        # Depuración:
        print("Email recibido:", email)
        print("Usuario encontrado:", user)
        if user:
            print("Password hash almacenado:", user.password_hash)
            print("¿Contraseña correcta?:", user.check_password(password))

        if user and user.check_password(password):
            login_user(user)
            flash('Inicio de sesión correcto', 'success')
            return redirect(url_for('categorias.listar_categorias'))
        else:
            flash('Usuario o contraseña incorrectos', 'danger')

    return render_template('auth/login.html')


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Sesión cerrada', 'info')
    return redirect(url_for('auth.login'))


@auth_bp.route('/registro', methods=['GET', 'POST'])
def registro():
    if current_user.is_authenticated:
        return redirect(url_for('categorias.listar_categorias'))

    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        password = request.form['password']

        if Usuario.query.filter_by(email=email).first():
            flash('El email ya está registrado', 'danger')
            return redirect(url_for('auth.registro'))

        nuevo_usuario = Usuario(nombre=nombre, email=email)
        nuevo_usuario.set_password(password)
        db.session.add(nuevo_usuario)
        db.session.commit()
        flash('Cuenta creada correctamente. Ahora puedes iniciar sesión.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('auth/register.html')
