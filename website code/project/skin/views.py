from django.shortcuts import render
from django.http import HttpResponse
from gradio_client import Client
import base64

def predict_image(request):
    if request.method == 'POST':

        uploaded_image = request.FILES['image']


        encoded_image = base64.b64encode(uploaded_image.read()).decode('utf-8')


        client = Client("https://zondl-skinscanner.hf.space/")


        result = client.predict(encoded_image, api_name="/predict")
        context={'result':result}


        return render(request, 'skin.html', context)
    else:
        return render(request, 'skin.html', )