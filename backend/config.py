class Config(object):
    DB_HOST = '127.0.0.1'
    DB_PORT = 5432
    DB_USER = 'postgres'
    DB_PASS = '123'
    DB_NAME = 'pixel_craft_db'

    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    UPLOAD_FOLDER = 'static/uploads/'
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # Use an in-memory SQLite database for testing
    SQLALCHEMY_TRACK_MODIFICATIONS = False
