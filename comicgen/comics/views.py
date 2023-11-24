from django.shortcuts import render
from .forms import ComicForm
import requests
from PIL import Image
import io
import base64

def generate_comics(request):
    strips = []
    if request.method == 'GET':
        form = ComicForm()
    else:
        form = ComicForm(request.POST)
        if form.is_valid():
            API_URL = "https://xdwvg9no7pefghrn.us-east-1.aws.endpoints.huggingface.cloud"
            headers = {
                "Accept": "image/png",
                "Authorization": "Bearer VknySbLLTUjbxXAXCjyfaFIPwUTCeRXbFSOjwRiCxsxFyhbnGjSFalPKrpvvDAaPVzWEevPljilLVDBiTzfIbWFdxOkYJxnOPoHhkkVGzAknaOulWggusSFewzpqsNWM",
                "Content-Type": "application/json"
            }
            text = form.cleaned_data['text']
            payload = {'inputs':text}
            def query(payload):
                response = requests.post(API_URL, headers=headers, json=payload)
                return response.content
            
            image_bytes = [query(payload) for i in range(1)]
            image_bytes_list = [Image.open(io.BytesIO(image_byte)) for image_byte in image_bytes]
            def image_to_data_uri(image, format='PNG'):
                buffer = io.BytesIO()
                image.save(buffer, format=format)
                image_data_uri = f'data:image/{format.lower()};base64,{base64.b64encode(buffer.getvalue()).decode()}'
                return image_data_uri
            
            strips = [image_to_data_uri(strip) for strip in image_bytes_list]

    return render(request,'index.html',{'form': form, 'strips': strips})
    
