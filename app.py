from flask import Flask
from persistence.ipersistence_manager import IPersistenceManager
from persistence.data_manager import DataManager
from model.user import User
from api.user_controller import user_controller
from api.amenity_controller import amenity_controller
from api.place_controller import place_controller
from api.review_controller import review_controller
from api.city_controller import city_controller
from api.country_controller import country_controller
import json

app = Flask(__name__)

@app.route("/")
def index():
    return "home"
    
app.register_blueprint(user_controller)
app.register_blueprint(amenity_controller)
app.register_blueprint(place_controller)
app.register_blueprint(review_controller)
app.register_blueprint(city_controller)
app.register_blueprint(country_controller)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)



