from bson.decimal128 import Decimal128
from bson import ObjectId
from datetime import datetime

def serialize_doc(doc):
    serialized_doc = {}
    for key, value in doc.items():
        if isinstance(value, ObjectId):
            serialized_doc[key] = str(value)
        elif isinstance(value, Decimal128):
            serialized_doc[key] = float(value.to_decimal())
        elif isinstance(value, datetime):
            serialized_doc[key] = value.isoformat()
        else:
            serialized_doc[key] = value
    return serialized_doc