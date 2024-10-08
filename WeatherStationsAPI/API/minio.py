from django.conf import settings
from minio import Minio
from django.core.files.uploadedfile import InMemoryUploadedFile
from rest_framework.response import *

def process_file_upload(file_object: InMemoryUploadedFile, client, image_name):
    try:
        client.put_object('weather-station-images', image_name, file_object, file_object.size)
        return f"http://localhost:9000/weather-station-images/{image_name}"
    except Exception as e:
        return {"error": str(e)}

def add_pic(station, pic):
    client = Minio(           
        endpoint=settings.AWS_S3_ENDPOINT_URL,
        access_key=settings.AWS_ACCESS_KEY_ID,
        secret_key=settings.AWS_SECRET_ACCESS_KEY,
        secure=settings.MINIO_USE_SSL
    )
    i = station.id
    img_obj_name = f"{i}.png"

    if not pic:
        return Response({"error": "Нет файла для изображения станции."})
    result = process_file_upload(pic, client, img_obj_name)

    if 'error' in result:
        return Response(result)

    station.photo_url = result
    station.save()

    return Response({"message": "success"})

def del_pic(station):
    client = Minio(           
        endpoint=settings.AWS_S3_ENDPOINT_URL,
        access_key=settings.AWS_ACCESS_KEY_ID,
        secret_key=settings.AWS_SECRET_ACCESS_KEY,
        secure=settings.MINIO_USE_SSL
    )
    i = station.id
    img_obj_name = f"{i}.png"
    try:
        client.remove_object('weather-station-images', img_obj_name)
    except Exception as e:
        return {"error": str(e)}