from flask import jsonify
from auto_app import app


@app.route('/api/v1/autos', methods=['GET'])
def get_autos():
    return jsonify({
        'success': True,
        'data': 'Get all autos'
    })


@app.route('/api/v1/autos', methods=['POST'])
def create_auto():
    return jsonify({
        'success': True,
        'data': 'New auto has been created'
    }), 201

