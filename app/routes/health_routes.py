from flask import Blueprint, current_app, jsonify, request
from bson import ObjectId
from ..utils.helpers import serialize_doc

app = Blueprint('health', __name__, url_prefix='/health')


# CRUD Operations for Animal_health
@app.route('/health', methods=['GET'])
def get_health_records():
    health_list = []
    for record in current_app.db['Animal_health'].find():
        health_list.append(serialize_doc(record))
    return jsonify(health_list), 200

@app.route('/health', methods=['POST'])
def add_health_record():
    new_record = request.json
    result = current_app.db['Animal_health'].insert_one(new_record)
    return jsonify({"message": "Health record added", "id": str(result.inserted_id)}), 201

@app.route('/health/<id>', methods=['GET'])
def get_health_record_by_id(id):
    record = current_app.db['Animal_health'].find_one({"_id": ObjectId(id)})
    return jsonify(serialize_doc(record)) if record else jsonify({"message": "Health record not found"}), 404

@app.route('/health/<id>', methods=['PUT'])
def update_health_record(id):
    updated_data = request.json
    result = current_app.db['Animal_health'].update_one({"_id": ObjectId(id)}, {"$set": updated_data})
    return jsonify({"message": "Health record updated"}), 200 if result.modified_count > 0 else 404

@app.route('/health/<id>', methods=['DELETE'])
def delete_health_record(id):
    result = current_app.db['Animal_health'].delete_one({"_id": ObjectId(id)})
    return jsonify({"message": "Health record deleted"}), 200 if result.deleted_count > 0 else 404
