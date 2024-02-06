from django.shortcuts import render, get_object_or_404
from .models import Dogs, Cats
from PIL import Image

# Create your views here.
def index(request):
	
	return render(request, "dog/index.html")

def dogs(request):
	dogs = Dogs.objects.all()
	return render(request, "dog/dogs.html", {
		"dogs": dogs
	})

def cats(request):
	cats = Cats.objects.all()
	return render(request, "dog/cats.html", {
		"cats": cats
	})

def about(request):
	return render(request, "dog/about.html")

def volunteer(request):
	return render(request, "dog/volunteer.html")

def donation(request):
	return render(request, "dog/donation.html")

def dog_info(request, dog_id):
    dog = get_object_or_404(Dogs, id=dog_id)
    return render(request, "dog/dog_info.html", {
        "dog": dog
            })
