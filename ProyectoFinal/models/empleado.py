from datetime import datetime
from app import db

class Empleado(db.Model):
    __tablename__ = 'empleados'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    cargo = db.Column(db.String(100), nullable=True)
    telefono = db.Column(db.String(20), nullable=True)
    fecha_nacimiento = db.Column(db.Date, nullable=True)
    dni = db.Column(db.String(20), unique=True, nullable=False)
    estado = db.Column(db.String(20), default='activo')
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    fecha_actualizacion = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Opcional: enlace a usuario, si quieres asociar credenciales de login a un empleado
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=True)
    usuario = db.relationship('Usuario', backref='empleado', uselist=False)