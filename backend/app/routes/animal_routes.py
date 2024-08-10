from flask import Blueprint, current_app, jsonify, request
from bson import ObjectId
from ..utils.helpers import serialize_doc

app = Blueprint('animals', __name__, url_prefix='/animals')

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
def add_animal():
    data = request.json

    # Insert into Species_info if not already present
    species_query = {"Species_name": data["Species_name"]}
    species = current_app.db["Species_info"].find_one(species_query)

    if not species:
        species_data = {
            "Species_name": data["Species_name"],
            "Species_type": data["Species_type"],
            "Species_lifespan": data["Species_lifespan"],
            "Food_type": data["Food_type"]
        }
        species_id = insert_document("Species_info", species_data)
    else:
        species_id = str(species["_id"])

    # Insert into Enclosure_info if not already present
    enclosure_query = {"Enclosure_name": data["Enclosure_name"]}
    enclosure = current_app.db["Enclosure_info"].find_one(enclosure_query)

    if not enclosure:
        enclosure_data = {
            "Enclosure_name": data["Enclosure_name"],
            "Enclosure_type": data["Enclosure_type"],
            "Enclosure_capacity": data["Enclosure_capacity"]
        }
        enclosure_id = insert_document("Enclosure_info", enclosure_data)
    else:
        enclosure_id = str(enclosure["_id"])

    # Insert into Animal_info
    animal_data = {
        "Species_id": ObjectId(species_id),
        "Animal_name": data["Animal_name"],
        "Animal_sex": data["Animal_sex"],
        "Animal_birthdate": datetime.strptime(data["Animal_birthdate"], "%Y-%m-%d"),
        "Current_animal_location": ObjectId(enclosure_id)
    }
    animal_id = insert_document("Animal_info", animal_data)

    # Insert into Animal_feeding
    feeding_data = {
        "Animal_id": ObjectId(animal_id),
        "Feeding_action_type": data["Feeding_action_type"],
        "Food_time": datetime.strptime(data["Food_time"], "%Y-%m-%dT%H:%M:%S.%f"),
        "Food_type": data["Food_type"],
        "Food_weight": data["Food_weight"]
    }
    insert_document("Animal_feeding", feeding_data)

    # Insert into Animal_health
    health_data = {
        "Animal_id": ObjectId(animal_id),
        "Health_event_type": data["Health_event_type"],
        "Health_event_time": datetime.strptime(data["Health_event_time"], "%a, %d %b %Y %H:%M:%S GMT"),
        "Health_event_comments": data["Health_event_comments"]
    }
    insert_document("Animal_health", health_data)

    return jsonify({"message": "Animal and related records added successfully", "Animal_id": animal_id}), 201

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
