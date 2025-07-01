# models/usuario.py o models/__init__.py
from extensions import db, login_manager

from .usuario import Usuario
from .empleado import Empleado
from .producto import Producto
from .categoria import Categoria

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))
__all__ = ['Usuario', 'Empleado', 'Producto', 'Categoria']