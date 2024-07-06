from flask import Blueprint, request, jsonify
from persistence.data_manager import DataManager
from datetime import datetime
from model.user import User
import json

user_controller = Blueprint('user_controller', __name__)
dmanager = DataManager()

@user_controller.route("/users" , methods=['POST'])
def user_post():
    data = request.get_json()
    email = data.get('email')
    first_name = data.get('first_name')
    last_name = data.get('last_name')

    if '@' not in email:
            return jsonify({'error': 'Invalid email format'}), 400
    with open('data.json', 'r') as data:
        dataStore = json.load(data)
    if "User" in dataStore:
        for user_info in dataStore["User"].values():
            if user_info["email"] == email:
                return jsonify({'error': 'Email already exists'}), 400
    
    usr = User(email, first_name, last_name)
    dmanager.save(usr)
    return jsonify(usr.__dict__), 201 

@user_controller.route("/users", methods=['GET'])
def user_get():
    with open('data.json', 'r') as data:
        dataStore = json.load(data)
    return jsonify(dataStore["User"]), 200


@user_controller.route("/users/<user_id>", methods=['GET'])
def user_get_id(user_id):
    return dmanager.get(user_id, "User")

@user_controller.route("/users/<user_id>", methods=['PUT'])
def user_update(user_id):
    data = request.get_json()
    existing_data = dmanager.get(user_id, 'User')
    if not existing_data:
        return jsonify({'error': 'User not found'}), 404


    """Create and update user without using **kwargs"""
    updated_user = User( data.get('email'), data.get('email'), data.get('email'))
    updated_user.id = user_id
    updated_user.created_at = existing_data["created_at"]
    dmanager.update(updated_user)
    return jsonify(updated_user.__dict__), 200



@user_controller.route("/users/<user_id>", methods=['DELETE'])
def user_delete(user_id):
    user = dmanager.get(user_id, 'User')
    if user is None:
        return jsonify({"error": "user not found"}), 404
    dmanager.delete(user_id, "User")
    return  jsonify({'message': 'User deleted'}), 204
    


