from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.sql import text
# from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
#
db = SQLAlchemy(app)
# migrate = Migrate(app, db)
#
# with app.app_context():
#     results = db.session.execute(text('show databases'))
# for row in results:
#     print(row)
# def create_app(config_class=Config):
#     app = Flask(__name__)
#     app.config.from_object(config_class)
#
#     db.init_app(app)
#     # migrate.init_app(app, db)
#     from auto_app.autos import autos_bp
#     app.register_blueprint(autos_bp)
#
#     return app
from auto_app import autos
# from auto_app import models

@app.route('/')
def index():
    return 'Hello from flask2'