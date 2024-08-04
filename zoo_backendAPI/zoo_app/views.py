# zoo_app/views.py
from django.http import JsonResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from bson.objectid import ObjectId
import json
from .mongo_client import db
from django.shortcuts import render

def home(request):
    return render(request, '../backendAPI_DB/zoo_backendAPI/zoo_app/templates/zoo_app/index.html')
# Helper function to convert ObjectId to string
def convert_objectid_to_str(doc):
    doc['_id'] = str(doc['_id'])
    return doc

# Helper function to handle not found errors
def find_one_or_404(collection, filter):
    document = collection.find_one(filter)
    if not document:
        return HttpResponseNotFound({'error': 'Not found'})
    return document

# Species_info Endpoints
@csrf_exempt
def handle_species_info(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        db.Species_info.insert_one(data)
        return JsonResponse({'msg': 'Species info created'}, status=201)
    else:
        species_info = db.Species_info.find()
        return JsonResponse([convert_objectid_to_str(info) for info in species_info], safe=False)

@csrf_exempt
def handle_species_info_detail(request, id):
    if request.method == 'GET':
        species_info = find_one_or_404(db.Species_info, {'_id': ObjectId(id)})
        if isinstance(species_info, HttpResponseNotFound):
            return species_info
        return JsonResponse(convert_objectid_to_str(species_info))
    elif request.method == 'PUT':
        data = json.loads(request.body)
        db.Species_info.update_one({'_id': ObjectId(id)}, {'$set': data})
        return JsonResponse({'msg': 'Species info updated'})
    else:
        db.Species_info.delete_one({'_id': ObjectId(id)})
        return JsonResponse({'msg': 'Species info deleted'})

# Animal_info Endpoints
@csrf_exempt
def handle_animal_info(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        db.Animal_info.insert_one(data)
        return JsonResponse({'msg': 'Animal info created'}, status=201)
    else:
        animal_info = db.Animal_info.find()
        return JsonResponse([convert_objectid_to_str(info) for info in animal_info], safe=False)

@csrf_exempt
def handle_animal_info_detail(request, id):
    if request.method == 'GET':
        animal_info = find_one_or_404(db.Animal_info, {'_id': ObjectId(id)})
        if isinstance(animal_info, HttpResponseNotFound):
            return animal_info
        return JsonResponse(convert_objectid_to_str(animal_info))
    elif request.method == 'PUT':
        data = json.loads(request.body)
        db.Animal_info.update_one({'_id': ObjectId(id)}, {'$set': data})
        return JsonResponse({'msg': 'Animal info updated'})
    else:
        db.Animal_info.delete_one({'_id': ObjectId(id)})
        return JsonResponse({'msg': 'Animal info deleted'})

# Animal_feeding Endpoints
@csrf_exempt
def handle_animal_feeding(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        db.Animal_feeding.insert_one(data)
        return JsonResponse({'msg': 'Animal feeding info created'}, status=201)
    else:
        animal_feeding = db.Animal_feeding.find()
        return JsonResponse([convert_objectid_to_str(feeding) for feeding in animal_feeding], safe=False)

@csrf_exempt
def handle_animal_feeding_detail(request, id):
    if request.method == 'GET':
        animal_feeding = find_one_or_404(db.Animal_feeding, {'_id': ObjectId(id)})
        if isinstance(animal_feeding, HttpResponseNotFound):
            return animal_feeding
        return JsonResponse(convert_objectid_to_str(animal_feeding))
    elif request.method == 'PUT':
        data = json.loads(request.body)
        db.Animal_feeding.update_one({'_id': ObjectId(id)}, {'$set': data})
        return JsonResponse({'msg': 'Animal feeding info updated'})
    else:
        db.Animal_feeding.delete_one({'_id': ObjectId(id)})
        return JsonResponse({'msg': 'Animal feeding info deleted'})

# Animal_health Endpoints
@csrf_exempt
def handle_animal_health(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        db.Animal_health.insert_one(data)
        return JsonResponse({'msg': 'Animal health info created'}, status=201)
    else:
        animal_health = db.Animal_health.find()
        return JsonResponse([convert_objectid_to_str(health) for health in animal_health], safe=False)

@csrf_exempt
def handle_animal_health_detail(request, id):
    if request.method == 'GET':
        animal_health = find_one_or_404(db.Animal_health, {'_id': ObjectId(id)})
        if isinstance(animal_health, HttpResponseNotFound):
            return animal_health
        return JsonResponse(convert_objectid_to_str(animal_health))
    elif request.method == 'PUT':
        data = json.loads(request.body)
        db.Animal_health.update_one({'_id': ObjectId(id)}, {'$set': data})
        return JsonResponse({'msg': 'Animal health info updated'})
    else:
        db.Animal_health.delete_one({'_id': ObjectId(id)})
        return JsonResponse({'msg': 'Animal health info deleted'})

# Enclosure_info Endpoints
@csrf_exempt
def handle_enclosure_info(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        db.Enclosure_info.insert_one(data)
        return JsonResponse({'msg': 'Enclosure info created'}, status=201)
    else:
        enclosure_info = db.Enclosure_info.find()
        return JsonResponse([convert_objectid_to_str(info) for info in enclosure_info], safe=False)

@csrf_exempt
def handle_enclosure_info_detail(request, id):
    if request.method == 'GET':
        enclosure_info = find_one_or_404(db.Enclosure_info, {'_id': ObjectId(id)})
        if isinstance(enclosure_info, HttpResponseNotFound):
            return enclosure_info
        return JsonResponse(convert_objectid_to_str(enclosure_info))
    elif request.method == 'PUT':
        data = json.loads(request.body)
        db.Enclosure_info.update_one({'_id': ObjectId(id)}, {'$set': data})
        return JsonResponse({'msg': 'Enclosure info updated'})
    else:
        db.Enclosure_info.delete_one({'_id': ObjectId(id)})
        return JsonResponse({'msg': 'Enclosure info deleted'})
