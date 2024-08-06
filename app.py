from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson import ObjectId  # Correctly import ObjectId
from dotenv import load_dotenv
import os


load_dotenv()

mongo_uri = os.getenv('MONGO_URI')
db_name = os.getenv('DATABASE_NAME')

app = Flask(__name__)

client = MongoClient(mongo_uri)

# Choose your database
db = client[db_name]

# Helper function to serialize documents
def serialize_doc(doc):
    if doc is not None:
        doc['_id'] = str(doc['_id'])  # Convert ObjectId to string
        # You can also convert other ObjectId fields here if necessary
    return doc

# Endpoint to test connection
@app.route('/test')
def test_connection():
    try:
        species = db['Species_info'].find_one()
        serialized_species = serialize_doc(species)
        if serialized_species:
            return jsonify({"message": "Connection successful", "species": serialized_species}), 200
        else:
            return jsonify({"message": "No species found"}), 404
    except Exception as e:
        return jsonify({"message": "Connection failed", "error": str(e)}), 500

# CRUD Operations for Species_info
@app.route('/species', methods=['GET'])
def get_species():
    species_list = []
    for species in db['Species_info'].find():
        species_list.append(serialize_doc(species))
    return jsonify(species_list), 200

@app.route('/species', methods=['POST'])
def add_species():
    new_species = request.json
    result = db['Species_info'].insert_one(new_species)
    return jsonify({"message": "Species added", "id": str(result.inserted_id)}), 201

@app.route('/species/<id>', methods=['GET'])
def get_species_by_id(id):
    species = db['Species_info'].find_one({"_id": ObjectId(id)})
    return jsonify(serialize_doc(species)) if species else jsonify({"message": "Species not found"}), 404

@app.route('/species/<id>', methods=['PUT'])
def update_species(id):
    updated_data = request.json
    result = db['Species_info'].update_one({"_id": ObjectId(id)}, {"$set": updated_data})
    return jsonify({"message": "Species updated"}), 200 if result.modified_count > 0 else 404

@app.route('/species/<id>', methods=['DELETE'])
def delete_species(id):
    result = db['Species_info'].delete_one({"_id": ObjectId(id)})
    return jsonify({"message": "Species deleted"}), 200 if result.deleted_count > 0 else 404

# CRUD Operations for Animal_info
@app.route('/animals', methods=['GET'])
def get_animals():
    animals_list = []
    for animal in db['Animal_info'].find():
        animals_list.append(serialize_doc(animal))
    return jsonify(animals_list), 200

@app.route('/animals', methods=['POST'])
def add_animal():
    new_animal = request.json
    result = db['Animal_info'].insert_one(new_animal)
    return jsonify({"message": "Animal added", "id": str(result.inserted_id)}), 201

@app.route('/animals/<id>', methods=['GET'])
def get_animal_by_id(id):
    animal = db['Animal_info'].find_one({"_id": ObjectId(id)})
    return jsonify(serialize_doc(animal)) if animal else jsonify({"message": "Animal not found"}), 404

@app.route('/animals/<id>', methods=['PUT'])
def update_animal(id):
    updated_data = request.json
    result = db['Animal_info'].update_one({"_id": ObjectId(id)}, {"$set": updated_data})
    return jsonify({"message": "Animal updated"}), 200 if result.modified_count > 0 else 404

@app.route('/animals/<id>', methods=['DELETE'])
def delete_animal(id):
    result = db['Animal_info'].delete_one({"_id": ObjectId(id)})
    return jsonify({"message": "Animal deleted"}), 200 if result.deleted_count > 0 else 404

# CRUD Operations for Animal_feeding
@app.route('/feeding', methods=['GET'])
def get_feeding_records():
    feeding_list = []
    for record in db['Animal_feeding'].find():
        feeding_list.append(serialize_doc(record))
    return jsonify(feeding_list), 200

@app.route('/feeding', methods=['POST'])
def add_feeding_record():
    new_record = request.json
    result = db['Animal_feeding'].insert_one(new_record)
    return jsonify({"message": "Feeding record added", "id": str(result.inserted_id)}), 201

@app.route('/feeding/<id>', methods=['GET'])
def get_feeding_record_by_id(id):
    record = db['Animal_feeding'].find_one({"_id": ObjectId(id)})
    return jsonify(serialize_doc(record)) if record else jsonify({"message": "Feeding record not found"}), 404

@app.route('/feeding/<id>', methods=['PUT'])
def update_feeding_record(id):
    updated_data = request.json
    result = db['Animal_feeding'].update_one({"_id": ObjectId(id)}, {"$set": updated_data})
    return jsonify({"message": "Feeding record updated"}), 200 if result.modified_count > 0 else 404

@app.route('/feeding/<id>', methods=['DELETE'])
def delete_feeding_record(id):
    result = db['Animal_feeding'].delete_one({"_id": ObjectId(id)})
    return jsonify({"message": "Feeding record deleted"}), 200 if result.deleted_count > 0 else 404

# CRUD Operations for Animal_health
@app.route('/health', methods=['GET'])
def get_health_records():
    health_list = []
    for record in db['Animal_health'].find():
        health_list.append(serialize_doc(record))
    return jsonify(health_list), 200

@app.route('/health', methods=['POST'])
def add_health_record():
    new_record = request.json
    result = db['Animal_health'].insert_one(new_record)
    return jsonify({"message": "Health record added", "id": str(result.inserted_id)}), 201

@app.route('/health/<id>', methods=['GET'])
def get_health_record_by_id(id):
    record = db['Animal_health'].find_one({"_id": ObjectId(id)})
    return jsonify(serialize_doc(record)) if record else jsonify({"message": "Health record not found"}), 404

@app.route('/health/<id>', methods=['PUT'])
def update_health_record(id):
    updated_data = request.json
    result = db['Animal_health'].update_one({"_id": ObjectId(id)}, {"$set": updated_data})
    return jsonify({"message": "Health record updated"}), 200 if result.modified_count > 0 else 404

@app.route('/health/<id>', methods=['DELETE'])
def delete_health_record(id):
    result = db['Animal_health'].delete_one({"_id": ObjectId(id)})
    return jsonify({"message": "Health record deleted"}), 200 if result.deleted_count > 0 else 404

# CRUD Operations for Enclosure_info
@app.route('/enclosures', methods=['GET'])
def get_enclosures():
    enclosure_list = []
    for enclosure in db['Enclosure_info'].find():
        enclosure_list.append(serialize_doc(enclosure))
    return jsonify(enclosure_list), 200

@app.route('/enclosures', methods=['POST'])
def add_enclosure():
    new_enclosure = request.json
    result = db['Enclosure_info'].insert_one(new_enclosure)
    return jsonify({"message": "Enclosure added", "id": str(result.inserted_id)}), 201

@app.route('/enclosures/<id>', methods=['GET'])
def get_enclosure_by_id(id):
    enclosure = db['Enclosure_info'].find_one({"_id": ObjectId(id)})
    return jsonify(serialize_doc(enclosure)) if enclosure else jsonify({"message": "Enclosure not found"}), 404

@app.route('/enclosures/<id>', methods=['PUT'])
def update_enclosure(id):
    updated_data = request.json
    result = db['Enclosure_info'].update_one({"_id": ObjectId(id)}, {"$set": updated_data})
    return jsonify({"message": "Enclosure updated"}), 200 if result.modified_count > 0 else 404

@app.route('/enclosures/<id>', methods=['DELETE'])
def delete_enclosure(id):
    result = db['Enclosure_info'].delete_one({"_id": ObjectId(id)})
    return jsonify({"message": "Enclosure deleted"}), 200 if result.deleted_count > 0 else 404

if __name__ == '__main__':
    app.run(debug=True)
