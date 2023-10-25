from django.urls import path
from . import views

urlpatterns = [
	path("", views.index, name="index"),
	path("dogs", views.dogs, name="dogs"),
	path("cats", views.cats, name="cats"),
    path("about", views.about, name="about")
]
