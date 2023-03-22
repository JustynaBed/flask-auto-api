from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

with app.app_context():
    results = db.session.execute(text('show databases'))
for row in results:
    print(row)


from auto_app import autos
@app.route('/')
def index():
    return 'Hello from flask2'