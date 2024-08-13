from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from config import Config

# Initialize the extensions
db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)  

    # from .views import mt,mst
    # app.register_blueprint(mt)
    # app.register_blueprint(mst)

    # from .models import MachineTypes
   
    return app

