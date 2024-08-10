from flask import Blueprint, current_app, jsonify, request
from bson import ObjectId
from ..utils.helpers import serialize_doc

app = Blueprint('animals', __name__, url_prefix='/animals')

# Utility function to insert a document and return the inserted ID
def insert_document(collection_name, document):
    result = current_app.db[collection_name].insert_one(document)
    return str(result.inserted_id)

# CRUD Operations for Animal_info
@app.route('/', methods=['GET'])
def get_animals():
    animals_list = []
    for animal in current_app.db['Animal_info'].find():
        animal_data = serialize_doc(animal)

        # Fetch species information
        species = current_app.db['Species_info'].find_one({"Species_name": animal_data['Species_name']})
        if species:
            animal_data['Species_info'] = serialize_doc(species)

        # Fetch enclosure information
        enclosure = current_app.db['Enclosure_info'].find_one({"Enclosure_name": animal_data['Current_animal_location']})
        if enclosure:
            animal_data['Enclosure_info'] = serialize_doc(enclosure)

        # Fetch feeding records
        feeding_records = current_app.db['Animal_feeding'].find({"Animal_id": animal_data['_id']})
        animal_data['Feeding_records'] = [serialize_doc(record) for record in feeding_records]

        # Fetch health records
        health_records = current_app.db['Animal_health'].find({"Animal_id": animal_data['_id']})
        animal_data['Health_records'] = [serialize_doc(record) for record in health_records]

        animals_list.append(animal_data)

    return jsonify(animals_list), 200

@app.route('/add_animal', methods=['POST'])
def insert_animal():
    data = request.json

    # Insert or update Species_info
    species_query = {"Species_name": data["Species_name"]}
    species_data = {
        "Species_name": data["Species_name"],
        "Species_type": data["Species_info"]["Species_type"],
        "Species_lifespan": data["Species_info"]["Species_lifespan"],
        "Food_type": data["Species_info"]["Food_type"],
        "Species_image_url": data["Species_info"]["Species_image_url"]
    }
    species = current_app.db["Species_info"].find_one_and_update(
        species_query, {"$set": species_data}, upsert=True, return_document=True
    )
    species_id = str(species["_id"])

    # Insert or update Enclosure_info
    enclosure_query = {"Enclosure_name": data["Enclosure_info"]["Enclosure_name"]}
    enclosure_data = {
        "Enclosure_name": data["Enclosure_info"]["Enclosure_name"],
        "Animal_capacity": data["Enclosure_info"]["Animal_capacity"],
        "Current_population": data["Enclosure_info"]["Current_population"],
        "Enclosure_condition": data["Enclosure_info"]["Enclosure_condition"],
        "Enclosure_location": data["Enclosure_info"]["Enclosure_location"]
    }
    enclosure = current_app.db["Enclosure_info"].find_one_and_update(
        enclosure_query, {"$set": enclosure_data}, upsert=True, return_document=True
    )
    enclosure_id = str(enclosure["_id"])

    # Insert Animal_info
    animal_data = {
        "Species_name": data["Species_name"],
        "Animal_name": data["Animal_name"],
        "Animal_sex": data["Animal_sex"],
        "Animal_birthdate": datetime.strptime(data["Animal_birthdate"], "%Y-%m-%dT%H:%M:%S"),
        "Current_animal_location": data["Current_animal_location"],
        "Enclosure_info": ObjectId(enclosure_id),
        "Species_info": ObjectId(species_id)
    }
    animal_id = current_app.db["Animal_info"].insert_one(animal_data).inserted_id

    # Insert Feeding_records
    for feeding_record in data["Feeding_records"]:
        feeding_data = {
            "Animal_id": animal_id,
            "Feeding_action_type": feeding_record["Feeding_action_type"],
            "Food_time": datetime.strptime(feeding_record["Food_time"], "%Y-%m-%dT%H:%M:%S.%f"),
            "Food_type": feeding_record["Food_type"],
            "Food_weight": feeding_record["Food_weight"],
            "Species_name": feeding_record["Species_name"]
        }
        current_app.db["Feeding_records"].insert_one(feeding_data)

    # Insert Health_records
    for health_record in data["Health_records"]:
        health_data = {
            "Animal_id": animal_id,
            "Health_check_date": datetime.strptime(health_record["Health_check_date"], "%Y-%m-%dT%H:%M:%S"),
            "Health_notes": health_record["Health_notes"],
            "Health_status": health_record["Health_status"],
            "Species_name": health_record["Species_name"]
        }
        current_app.db["Health_records"].insert_one(health_data)

    return jsonify({"message": "Animal and related records added successfully", "Animal_id": str(animal_id)}), 201

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
