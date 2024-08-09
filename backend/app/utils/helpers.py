from bson import ObjectId

def serialize_doc(doc):
    if doc is not None:
        doc['_id'] = str(doc['_id'])
    return doc