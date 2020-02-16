from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
import django.template.loader as loader
from imageToText import detect_text
import sys
from .models import PhotoUploader
from PIL import Image


# Create your views here.
@csrf_exempt
def upload_image(request):
    if request.method == "POST":
        uploaded_file = request.FILES['document'] 
        print(uploaded_file.name)

        image = PhotoUploader(name = uploaded_file.name, image = uploaded_file)
        image.save()
        print("image full path", image.image.path)
        detect_text(image.image.path)
        
        # 'document' is the input name in the html
        # the value of request.FILES['document'] is an object of the type UploadedFiles

        # perhaps look into using generator for this? since it will be a large number of text, and ideally don't want to use memory
        # to store it
        
        return render(request, 'index3.html')
    else:
        return render(request, "index3.html")