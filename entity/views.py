from django.shortcuts import render


from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from entity.models import Entity
from entity.serializers import EntitySerializers

# Create your views here.
def entityApi(request,id):
    if request.method=='GET':
        entities = Entity.object.all()
        entities_serializer=EntitySerializers(Entity, many=True)
        return JsonResponse(entities_serializer.data, safe=False)
    elif request.method=='POST':
        entity_data = JSONParser().parse(request)
        entities_serializer=EntitySerializers(data=entity_data)
        if entities_serializer.is_valid():
            entities_serializer.save()
            return JSONParser("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        entity_data = JSONParser().parse(request)
        entity = Entity.objects.get(EntityID=entity_data['EntityID'])
        entities_serializer=EntitySerializers(entity, data=entity_data)
        if entities_serializer.is_valid():
            entities_serializer.save()
            return JSONParser("Updated Successfully", safe=False)
        return  JsonResponse("Failed to Update", safe=False)
    elif request.method=='DELETE':
        entity = Entity.objects.get(EntityID=id)
        entity.delete()
        return JsonResponse("Delete Successfully", safe=False)