from django.shortcuts import render
from django.http import HttpResponse
from .models import Image,Category,Location

# Create your views here.
def index(request):
    pics = Image.get_all()
    return render(request, 'index.html', {"pics": pics})

def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Category.search_by_category(search_term)
        images = Image.get_image_by_category(searched_images)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message, "image": images})

    else:
        message = "That category does not exist"
        return render(request, 'search.html', {"message": message})
