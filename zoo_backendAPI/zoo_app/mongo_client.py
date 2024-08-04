# zoo_app/mongo_client.py
from pymongo import MongoClient
from django.conf import settings

client = MongoClient(settings.MONGO_URI)
db = client.get_database()
