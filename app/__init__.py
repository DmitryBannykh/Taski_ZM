from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_swagger_ui import get_swaggerui_blueprint


db = SQLAlchemy()
ma = Marshmallow()


def create_app():
    """Фабричная функция для создания и настройки Flask-приложения."""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///memory.db' 
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost/mydatabase'  # Настройка URI для подключения к базе данных
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  
    db.init_app(app)
    ma.init_app(app)

    # swagger specific
    SWAGGER_URL = '/swagger'
    API_URL = '/static/swagger.yaml'
    SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "TASKI_ZM"
        }
    )
    app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
    #  end swagger specific

    with app.app_context():
        db.create_all()

    from .routes import init_routes
    init_routes(app)

    return app
