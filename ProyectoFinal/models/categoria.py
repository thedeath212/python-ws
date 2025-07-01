from app import db

class Categoria(db.Model):
    __tablename__ = 'categorias'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False, unique=True)
    descripcion = db.Column(db.Text)

    # Relación uno a muchos con Producto
    productos = db.relationship(
        'Producto',
        back_populates='categoria',
        lazy=True
    )
