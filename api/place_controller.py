from flask import Blueprint, request, jsonify
from persistence.data_manager import DataManager
from datetime import datetime
from model.place import Place
import json

place_controller = Blueprint('place_controller', __name__)
dmanager = DataManager() 

@place_controller.route("/places" , methods=['POST'])
def post_place():
    data = request.get_json()
    description = data.get('description')
    address = data.get('address')
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    host_id = data.get('host_id')
    city_id = data.get('city_id')
    number_of_rooms = data.get('number_of_rooms')
    number_of_bathrooms = data.get('number_of_bathrooms')
    price_per_night = data.get('price_per_night')
    max_guests = data.get('max_guests')
    amenity_ids = data.get('amenity_ids')
    name = data.get('name')

    if not name:
        return jsonify({"error": "Name is required"}), 400  


    # Create Place object with all attributes
    place = Place(name, description, address, city_id, latitude, longitude, host_id, number_of_rooms, number_of_bathrooms, price_per_night, max_guests, amenity_ids)
    dmanager.save(place)
    return jsonify(place.__dict__), 201


@place_controller.route("/places", methods=['GET'])
def get_place():
    with open('data.json', 'r') as data:
        dataStore = json.load(data)
    if dataStore is None:
        return jsonify({"error": "Place not found"}), 404
    else:
        return jsonify(dataStore["Place"]), 200

@place_controller.route("/places/<place_id>", methods=['GET'])
def get_place_id(place_id):
    place_data = dmanager.get(place_id, 'Place')
    if place_data is None:
        return jsonify({"error": "Place not found"}), 404
    else:
        return jsonify(place_data), 200


@place_controller.route('/places/<place_id>', methods=['PUT'])
def update_place(place_id):
    data = request.get_json()
    place_data = dmanager.get(entity_id=place_id, entity_type='Place')

    data = request.get_json()
    description = data.get('description')
    address = data.get('address')
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    host_id = data.get('host_id')
    city_id = data.get('city_id')
    number_of_rooms = data.get('number_of_rooms')
    number_of_bathrooms = data.get('number_of_bathrooms')
    price_per_night = data.get('price_per_night')
    max_guests = data.get('max_guests')
    amenity_ids = data.get('amenity_ids')
    name = data.get('name')

    if not name:
        return jsonify({"error": "Name is required"}), 400  


    # Create Place object with all attributes
    place = Place(name, description, address, city_id, latitude, longitude, host_id, number_of_rooms, number_of_bathrooms, price_per_night, max_guests, amenity_ids)
    
    place.id = place_id
    place.created_at = place_data["created_at"]
    
    # Save the updated place using your DataManager
    dmanager.update(place)
    return jsonify(place.__dict__), 200


@place_controller.route("/places/<place_id>", methods=['DELETE'])
def places_del(place_id):
    if dmanager.get(place_id, 'Place') is None:
        return jsonify({"error": "user not found"}), 404
    dmanager.delete(place_id, "Place")
    return  jsonify({'message': 'User deleted'}), 204
    

    



