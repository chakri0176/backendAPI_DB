from flask import Flask
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    app = Flask(__name__)

    mongo_uri = os.getenv('MONGO_URI')
    db_name = os.getenv('DATABASE_NAME')

    client = MongoClient(mongo_uri)
    app.db = client[db_name]

    from .routes import species_routes, animal_routes, feeding_routes, health_routes, enclosure_routes

    app.register_blueprint(species_routes.bp)
    app.register_blueprint(animal_routes.bp)
    app.register_blueprint(feeding_routes.bp)
    app.register_blueprint(health_routes.bp)
    app.register_blueprint(enclosure_routes.bp)

    return app