import json
from pathlib import Path
from sqlalchemy.sql import text

from auto_app import app, db
from auto_app.models import Auto

@app.cli.group()
def db_manage():
    """Database management commands"""
    pass

@db_manage.command()
def add_data():
    """Add sample data to database"""
    try:
        autos_path = Path(__file__).parent / 'samples' / 'autos.json'
        with open(autos_path) as file:
            data_json = json.load(file)
        for item in data_json:
            auto = Auto(**item)
            db.session.add(auto)
            db.session.commit()
        print('Data has been successfully added to database')
    except Exception as exc:
        print('Unexpected error: {}'.format(exc))
@db_manage.command()
def remove_data():
    """Remove all data from database"""
    try:
        query = text('TRUNCATE autos')
        db.session.execute(query)
        db.session.commit()
        print('Data has been succesfully remove from database')
    except Exception as exc:
        print('BŁĄD Unexpected error: {}'.format(exc))

