from django.shortcuts import render
from .models import Dogs, Cats
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
