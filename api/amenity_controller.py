from flask import Blueprint, request, jsonify
from persistence.data_manager import DataManager
from datetime import datetime
from model.amenity import Amenities
import json

amenity_controller = Blueprint('amenity_controller', __name__)
dmanager = DataManager()


@amenity_controller.route("/amenities", methods=['POST'])
def amenity_post():
    data = request.get_json()
    name = data.get('name')
    if not name:
        return jsonify({"error": "Name is required"}), 400
    amenity = Amenities(name)
    dmanager.save(amenity)
    return jsonify(amenity.__dict__), 201



@amenity_controller.route("/amenities", methods=['GET'])
def amenities1():
    with open('data.json', 'r') as data:
        dataStore = json.load(data)
    return dataStore["Amenities"], 200


@amenity_controller.route("/amenities/<amenity_id>", methods=['GET'])
def get_amenity(amenity_id):
    amenity_data = dmanager.get(amenity_id, 'Amenities')
    if dmanager.get(amenity_id, 'Amenities') is None:
        return jsonify({"error": "Amenity id not found"}), 404
    else:
        return jsonify(amenity_data), 200


@amenity_controller.route('/amenities/<amenity_id>', methods=['PUT'])
def update_amenity(amenity_id):
    data = request.get_json()
    existing_amenity = dmanager.get(amenity_id, 'Amenities')
    if existing_amenity is None:
        return jsonify({"error": "Amenity is not found"}), 404

    updated_amenity = Amenities(data.get('name'))
    updated_amenity.id = amenity_id
    updated_amenity.created_at = existing_amenity["created_at"]
    dmanager.update(updated_amenity)
    return jsonify(updated_amenity.__dict__), 200


@amenity_controller.route("/amenities/<amenity_id>", methods=['DELETE'])
def amenitie_del(amenity_id):
    if dmanager.get(amenity_id, 'Amenities') is None:
        return jsonify({"error": "Amenity is not found at all"}), 404
    dmanager.delete(amenity_id, 'Amenities')
    return jsonify({'message': 'Amenity deleted'}), 204

