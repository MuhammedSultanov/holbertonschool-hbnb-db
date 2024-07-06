from flask import Blueprint, request, jsonify
from persistence.data_manager import DataManager
from datetime import datetime
from model.review import Review
import json


review_controller = Blueprint('review_controller', __name__)
dmanager = DataManager()



@review_controller.route("/places/<place_id>/reviews" , methods=['POST'])
def review_post(place_id):
    data = request.get_json()
    user_id = data.get('user_id')
    rating = data.get('rating')
    comment = data.get('comment')
    rev = Review(place_id, user_id, rating, comment)
    dmanager.save(rev)
    return jsonify(rev.__dict__), 201


@review_controller.route("/users/<user_id>/reviews", methods=['GET'])
def review_get_userid(user_id):
    with open('data.json', 'r') as data:
        dataStore = json.load(data)
    user_id_to_search = user_id
    reviews_for_user = {key: value for key, value in dataStore["Review"].items() if value["user_id"] == user_id_to_search}
    return jsonify(reviews_for_user), 200


@review_controller.route("/places/<place_id>/reviews", methods=['GET'])
def review_get_placeid(place_id):
    with open('data.json', 'r') as data:
        dataStore = json.load(data)
    place_id_to_search = place_id
    reviews_for_place = {key: value for key, value in dataStore["Review"].items() if value["place_id"] == place_id_to_search}
    return jsonify(reviews_for_place), 200

@review_controller.route("/reviews/<review_id>", methods=['GET'])
def review_by_id(review_id):
    review = dmanager.get(review_id, 'Review')
    if review is None:
        return jsonify({"error": "revew not found"}), 404
    else:
        return jsonify(review), 200


@review_controller.route('/reviews/<review_id>', methods=['PUT'])
def update_review(review_id):
    data = request.get_json()
    existing_review = dmanager.get(review_id, 'Review')
    if existing_review is None:
        return jsonify({"error": "Amenity is not found"}), 404

    updated_review = Review(data.get('place_id'), data.get('user_id'), data.get('rating'), data.get('comment'))
    updated_review.id = review_id
    updated_review.created_at = existing_review["created_at"]
    dmanager.update(updated_review)
    return jsonify(updated_review.__dict__), 200



@review_controller.route("/reviews/<review_id>", methods=['DELETE'])
def amenitie_del(review_id):
    if dmanager.get(review_id, 'Review') is None:
        return jsonify({"error": "Review is not found at all"}), 404
    dmanager.delete(review_id, 'Review')
    return jsonify({'message': 'Review deleted'}), 204


