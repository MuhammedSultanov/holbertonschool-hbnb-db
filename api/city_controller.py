from flask import Blueprint, request, jsonify
from persistence.data_manager import DataManager
from datetime import datetime
from model.city import City
import json

city_controller = Blueprint('city_controller', __name__)
dmanager = DataManager()



@city_controller.route("/countries/<country_code>/cities" , methods=['GET'])
def city_(country_code):
    with open('data.json', 'r') as data:
        dataStore = json.load(data)
    city_with_code = country_code
    cities= {key: value for key, value in dataStore["City"].items() if value["country_code"] == city_with_code}
    return cities

@city_controller.route("/cities" , methods=['POST'])
def post_city():
    data = request.get_json()
    name = data.get('name')
    country_code = data.get('country_code')
    city = City(name, country_code)
    dmanager.save(city)
    return jsonify(city.__dict__), 201


@city_controller.route("/cities", methods=['GET'])
def city1():
    with open('data.json', 'r') as data:
        dataStore = json.load(data)
    return dataStore["City"]


@city_controller.route("/cities/<cities_id>", methods=['GET'])
def city_all(cities_id):
    city = dmanager.get(cities_id, 'City')
    if city is None:
        return jsonify({'error': 'City not found'}), 404
    else:
        return jsonify(city), 200

@city_controller.route('/cities/<cities_id>', methods=['PUT'])
def update_city(cities_id):
    data = request.get_json()
    existing_city = dmanager.get(cities_id, 'City')
    if existing_city is None:
        return jsonify({"error": "Amenity is not found"}), 404
    updated_city = City(data.get('name'), data.get('country_code'))
    updated_city.id = cities_id
    updated_city.created_at = existing_city["created_at"]
    dmanager.update(updated_city)
    return jsonify(updated_city.__dict__), 200

@city_controller.route("/cities/<cities_id>", methods=['DELETE'])
def city_del(cities_id):
    if dmanager.get(cities_id, 'City') is None:
        return jsonify({"error": "City is not found at all"}), 404
    dmanager.delete(cities_id, 'City')
    return jsonify({'message': 'City deleted'}), 204

