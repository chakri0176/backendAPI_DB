from flask import Blueprint, jsonify, request
from bson import ObjectId
from ..utils.helpers import serialize_doc

bp = Blueprint('species', __name__, url_prefix='/species')

@bp.route('/', methods=['GET'])
def get_species():
    species_list = []
    for species in current_app.db['Species_info'].find():
        species_list.append(serialize_doc(species))
    return jsonify(species_list), 200

# Add other species routes here...