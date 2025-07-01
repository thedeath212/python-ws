from app import db

class Producto(db.Model):
    __tablename__ = 'productos'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    precio = db.Column(db.Float, nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    imagen = db.Column(db.String(255), nullable=True)

    categoria_id = db.Column(
        db.Integer,
        db.ForeignKey('categorias.id'),
        nullable=False
    )

    # Relación muchos a uno con Categoria
    categoria = db.relationship(
        'Categoria',
        back_populates='productos'
    )
