from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.apps import apps
from importlib import import_module


@api_view(['DELETE'])
def delete(request, model_name, pk):
    try:
        model = apps.get_model('api', model_name)
    except LookupError:
        return Response({"error": "Model not found."}, status=status.HTTP_400_BAD_REQUEST)

    item = get_object_or_404(model, pk=pk)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['POST'])
def update(request, model_name, pk):
    ModelClass = apps.get_model('api', model_name)
    SerializerClass = getattr(import_module("api.serializers"), f"{model_name}Serializer")

    item = get_object_or_404(ModelClass, pk=pk)
    data = SerializerClass(instance=item, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view(request, model_name):
    ModelClass = apps.get_model('api', model_name)
    SerializerClass = getattr(import_module("api.serializers"), f"{model_name}Serializer")

    limit = int(request.query_params.get('limit', 5))  # Default limit to 5 if not provided

    # Fetch items with a limit
    query_params = request.query_params.dict()
    query_params.pop('limit', None)  # Remove 'limit' from query params if exists

    items = ModelClass.objects.filter(**query_params)[:limit]

    if items:
        serializer = SerializerClass(items, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def add(request, model_name):
    ModelClass = apps.get_model('api', model_name)
    SerializerClass = getattr(import_module("api.serializers"), f"{model_name}Serializer")

    item = SerializerClass(data=request.data)

    # if ModelClass.objects.filter(**request.data).exists():
    #     raise serializers.ValidationError('This data already exists')

    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_items': '/',
        'Add': '/add',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete'
    }

    return Response(api_urls)
