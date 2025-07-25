from flask import Blueprint, current_app, jsonify, request
from bson import ObjectId
from app.utils.helpers import serialize_doc

app = Blueprint('species', __name__, url_prefix='/species')

@app.route('/test', methods=['GET'])
def test_connection():
    try:
        species = current_app.db['Species_info'].find_one()
        serialized_species = serialize_doc(species)
        if serialized_species:
            return jsonify({"message": "Connection successful", "species": serialized_species}), 200
        else:
            return jsonify({"message": "No species found"}), 404
    except Exception as e:
        return jsonify({"message": "Connection failed", "error": str(e)}), 500

# CRUD Operations for Species_info
@app.route('/', methods=['GET'])
def get_species():
    species_list = []
    for species in current_app.db['Species_info'].find():
        species_list.append(serialize_doc(species))
    return jsonify(species_list), 200

@app.route('/', methods=['POST'])
def add_species():
    new_species = request.json
    result = current_app.db['Species_info'].insert_one(new_species)
    return jsonify({"message": "Species added", "id": str(result.inserted_id)}), 201

@app.route('/list', methods=['POST'])
def add_species_list():
    species_list = request.json
    
    if not isinstance(species_list, list):
        return jsonify({"message": "Invalid input, expected a list of species"}), 400
    
    if not all(isinstance(species, dict) for species in species_list):
        return jsonify({"message": "Invalid input, all items should be dictionaries"}), 400
    
    # Insert each species into the database
    ids = []
    for species in species_list:
        result = current_app.db['Species_info'].insert_one(species)
        ids.append(str(result.inserted_id))
    
    return jsonify({"message": "Species added", "ids": ids}), 201

@app.route('/<id>', methods=['GET'])
def get_species_by_id(id):
    species = current_app.db['Species_info'].find_one({"_id": ObjectId(id)})
    return jsonify(serialize_doc(species)) if species else jsonify({"message": "Species not found"}), 404

@app.route('/<id>', methods=['PUT'])
def update_species(id):
    updated_data = request.json
    result = current_app.db['Species_info'].update_one({"_id": ObjectId(id)}, {"$set": updated_data})
    return jsonify({"message": "Species updated"}), 200 if result.modified_count > 0 else 404

@app.route('/<id>', methods=['DELETE'])
def delete_species(id):
    result = current_app.db['Species_info'].delete_one({"_id": ObjectId(id)})
    return jsonify({"message": "Species deleted"}), 200 if result.deleted_count > 0 else 404
