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
