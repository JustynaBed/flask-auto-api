from flask import Flask
from config import Config
from auto_app import autos

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    return 'Hello from flask'