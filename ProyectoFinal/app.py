from flask import Flask, redirect, url_for
from config import Config
from extensions import db, login_manager  # importas extensiones

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    from models import Usuario  # Importar modelos aquí, después de init_app

    @login_manager.user_loader
    def load_user(user_id):
        return Usuario.query.get(int(user_id))

    # Importar blueprints dentro para evitar ciclos
    from routes.categorias import categorias_bp
    from routes.auth import auth_bp
    from routes.usuarios import usuarios_bp
    from routes.empleados import empleados_bp
    from routes.productos import productos_bp

    app.register_blueprint(categorias_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(usuarios_bp)
    app.register_blueprint(empleados_bp)
    app.register_blueprint(productos_bp)

    @app.route('/')
    def index():
        return redirect(url_for('auth.login'))

    return app

if __name__ == '__main__':
    app = create_app()
    print("🔐 Base de datos conectada a:", app.config['SQLALCHEMY_DATABASE_URI'])
    print("🔐 Clave secreta cargada:", app.config['SECRET_KEY'])
    app.run(debug=True)
