from flask import Blueprint

autos_bp = Blueprint('autos', __name__)


from auto_app.autos import autos
