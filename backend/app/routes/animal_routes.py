from flask import Blueprint, current_app, jsonify, request
from bson import ObjectId
from ..utils.helpers import serialize_doc

app = Blueprint('animals', __name__, url_prefix='/animals')

# CRUD Operations for Animal_info
@app.route('/', methods=['GET'])
def get_animals():
    animals_list = []
    for animal in current_app.db['Animal_info'].find():
        animals_list.append(serialize_doc(animal))
    return jsonify(animals_list), 200

@app.route('/', methods=['POST'])
def add_animal():
    new_animal = request.json
    result = current_app.db['Animal_info'].insert_one(new_animal)
    return jsonify({"message": "Animal added", "id": str(result.inserted_id)}), 201

@app.route('/<id>', methods=['GET'])
def get_animal_by_id(id):
    animal = current_app.db['Animal_info'].find_one({"_id": ObjectId(id)})
    return jsonify(serialize_doc(animal)) if animal else jsonify({"message": "Animal not found"}), 404

@app.route('/<id>', methods=['PUT'])
def update_animal(id):
    updated_data = request.json
    result = current_app.db['Animal_info'].update_one({"_id": ObjectId(id)}, {"$set": updated_data})
    return jsonify({"message": "Animal updated"}), 200 if result.modified_count > 0 else 404

@app.route('/<id>', methods=['DELETE'])
def delete_animal(id):
    result = current_app.db['Animal_info'].delete_one({"_id": ObjectId(id)})
    return jsonify({"message": "Animal deleted"}), 200 if result.deleted_count > 0 else 404
