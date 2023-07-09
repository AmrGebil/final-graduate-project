from django.shortcuts import render
from django.http import HttpResponse
from gradio_client import Client
import base64

def predict_image(request):
    if request.method == 'POST':
        # Retrieve the uploaded image file from the POST request
        uploaded_image = request.FILES['image']

        # Read the uploaded image file and encode it as base64
        encoded_image = base64.b64encode(uploaded_image.read()).decode('utf-8')

        # Create an instance of the Gradio Client
        client = Client("https://zondl-skinscanner.hf.space/")

        # Send the prediction request to the Gradio server
        result = client.predict(encoded_image, api_name="/predict")
        context={'result':result}

        # Process the result and return a response
        return render(request, 'skin.html', context)
    else:
        return render(request, 'skin.html', )