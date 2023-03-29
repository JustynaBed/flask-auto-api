from flask import Flask, render_template
from config import Config
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.sql import text
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__, template_folder='../dist')
app.config.from_object(Config)
CORS(app)

#
db = SQLAlchemy(app)
migrate = Migrate(app, db)
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
from auto_app import models
from auto_app import db_manage_commands

@app.route('/')
def index():
    return render_template('index.html')

