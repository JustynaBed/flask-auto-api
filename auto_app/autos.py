from flask import jsonify, request
from auto_app import app, db
# from auto_app.autos import autos_bp
from auto_app.models import Auto, AutoSchema, auto_schema


@app.route('/api/v1/autos', methods=['GET'])
def get_autos():
    autos = Auto.query.all()
    autos_schema = AutoSchema(many=True)
    return jsonify({
        'success': True,
        'data': autos_schema.dump(autos),
        'number_of_records': len(autos)
    })


@app.route('/api/v1/autos/<int:auto_id>', methods=['GET'])
def get_author(auto_id: int):
    auto = Auto.query.get_or_404(auto_id, description=f'Auto with id {auto_id} not found')
    return jsonify({
        'success': True,
        'data': auto_schema.dump(auto)
    })


@app.route('/api/v1/autos', methods=['POST'])
def create_auto():
    data = request.get_json()
    brand = data.get('brand')
    model = data.get('model')
    year = data.get('year')
    auto = Auto(brand=brand, model=model, year=year)
    db.session.add(auto)
    db.session.commit()
    return jsonify({
        'success': True,
        'data': auto_schema.dump(auto)
    }), 201

