from flask import Flask
from config import Config

app = Flask(__name__)
# app.config.from_object(Config)
# configg=app.config.from_object(Config)


from auto_app import autos
@app.route('/')
def index():
    return 'Hello from flask2'