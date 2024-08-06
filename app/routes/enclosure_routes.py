from flask import Blueprint, current_app, jsonify, request
from bson import ObjectId
from ..utils.helpers import serialize_doc

app = Blueprint('enclosures', __name__, url_prefix='/enclosures')

# CRUD Operations for Enclosure_info
@app.route('/enclosures', methods=['GET'])
def get_enclosures():
    enclosure_list = []
    for enclosure in current_app.db['Enclosure_info'].find():
        enclosure_list.append(serialize_doc(enclosure))
    return jsonify(enclosure_list), 200

@app.route('/enclosures', methods=['POST'])
def add_enclosure():
    new_enclosure = request.json
    result = current_app.db['Enclosure_info'].insert_one(new_enclosure)
    return jsonify({"message": "Enclosure added", "id": str(result.inserted_id)}), 201

@app.route('/enclosures/<id>', methods=['GET'])
def get_enclosure_by_id(id):
    enclosure = current_app.db['Enclosure_info'].find_one({"_id": ObjectId(id)})
    return jsonify(serialize_doc(enclosure)) if enclosure else jsonify({"message": "Enclosure not found"}), 404

@app.route('/enclosures/<id>', methods=['PUT'])
def update_enclosure(id):
    updated_data = request.json
    result = current_app.db['Enclosure_info'].update_one({"_id": ObjectId(id)}, {"$set": updated_data})
    return jsonify({"message": "Enclosure updated"}), 200 if result.modified_count > 0 else 404

@app.route('/enclosures/<id>', methods=['DELETE'])
def delete_enclosure(id):
    result = current_app.db['Enclosure_info'].delete_one({"_id": ObjectId(id)})
    return jsonify({"message": "Enclosure deleted"}), 200 if result.deleted_count > 0 else 404
