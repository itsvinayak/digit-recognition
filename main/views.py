from django.shortcuts import render
import base64
import json
import tensorflow as tf
from io import BytesIO
from django.http import JsonResponse

def index(request):
    return render(request,'main/index.html')


def getImg(request):
    data_image = request.POST.get('image')
    data_image = json.loads(data_image)
    postImg = BytesIO(base64.urlsafe_b64decode(data_image))

    # reading models
    #model = tf.keras.models.load_model('epic_num_reader.h5')
    print(postImg)
       
    return JsonResponse({})
