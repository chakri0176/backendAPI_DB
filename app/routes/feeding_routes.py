from flask import Blueprint, current_app, jsonify, request
from bson import ObjectId
from ..utils.helpers import serialize_doc

app = Blueprint('feeding', __name__, url_prefix='/feeding')


# CRUD Operations for Animal_feeding
@app.route('/feeding', methods=['GET'])
def get_feeding_records():
    feeding_list = []
    for record in current_app.db['Animal_feeding'].find():
        feeding_list.append(serialize_doc(record))
    return jsonify(feeding_list), 200

@app.route('/feeding', methods=['POST'])
def add_feeding_record():
    new_record = request.json
    result = current_app.db['Animal_feeding'].insert_one(new_record)
    return jsonify({"message": "Feeding record added", "id": str(result.inserted_id)}), 201

@app.route('/feeding/<id>', methods=['GET'])
def get_feeding_record_by_id(id):
    record = current_app.db['Animal_feeding'].find_one({"_id": ObjectId(id)})
    return jsonify(serialize_doc(record)) if record else jsonify({"message": "Feeding record not found"}), 404

@app.route('/feeding/<id>', methods=['PUT'])
def update_feeding_record(id):
    updated_data = request.json
    result = current_app.db['Animal_feeding'].update_one({"_id": ObjectId(id)}, {"$set": updated_data})
    return jsonify({"message": "Feeding record updated"}), 200 if result.modified_count > 0 else 404

@app.route('/feeding/<id>', methods=['DELETE'])
def delete_feeding_record(id):
    result = current_app.db['Animal_feeding'].delete_one({"_id": ObjectId(id)})
    return jsonify({"message": "Feeding record deleted"}), 200 if result.deleted_count > 0 else 404
