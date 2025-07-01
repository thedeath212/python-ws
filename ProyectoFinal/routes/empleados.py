from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from models.empleado import Empleado
from flask_login import login_required, current_user
from datetime import datetime

empleados_bp = Blueprint('empleados', __name__, url_prefix='/empleados')

@empleados_bp.route('/')
def listar_empleados():
    empleados = Empleado.query.all()
    return render_template('empleados/listar.html', empleados=empleados)

@empleados_bp.route('/nuevo', methods=['GET', 'POST'])
@login_required
def nuevo_empleado():
    if request.method == 'POST':
        nombre = request.form['nombre']
        cargo = request.form['cargo']
        telefono = request.form['telefono']
        fecha_nacimiento = request.form['fecha_nacimiento']
        dni = request.form['dni']
        estado = request.form.get('estado', 'activo')

        empleado = Empleado(
            nombre=nombre,
            cargo=cargo,
            telefono=telefono,
            dni=dni,
            estado=estado
        )
        if fecha_nacimiento:
            empleado.fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%Y-%m-%d').date()

        db.session.add(empleado)
        db.session.commit()
        flash('Empleado creado correctamente.', 'success')
        return redirect(url_for('empleados.listar_empleados'))

    return render_template('empleados/nuevo.html')

@empleados_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def editar_empleado(id):

    empleado = Empleado.query.get_or_404(id)
    if request.method == 'POST':
        empleado.nombre = request.form['nombre']
        empleado.cargo = request.form['cargo']
        empleado.telefono = request.form['telefono']
        empleado.dni = request.form['dni']
        empleado.estado = request.form.get('estado', empleado.estado)
        fecha_nacimiento = request.form['fecha_nacimiento']
        if fecha_nacimiento:
            empleado.fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%Y-%m-%d').date()
        db.session.commit()
        flash('Empleado actualizado.', 'success')
        return redirect(url_for('empleados.listar_empleados'))

    return render_template('empleados/editar.html', empleado=empleado)

@empleados_bp.route('/eliminar/<int:id>', methods=['POST'])
@login_required
def eliminar_empleado(id):
    if current_user.rol != 'admin':
        flash("No tienes permiso.", "danger")
        return redirect(url_for('index'))
    empleado = Empleado.query.get_or_404(id)
    db.session.delete(empleado)
    db.session.commit()
    flash('Empleado eliminado.', 'success')
    return redirect(url_for('empleados.listar_empleados'))
