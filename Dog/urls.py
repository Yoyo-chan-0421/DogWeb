from django.urls import path
from . import views

urlpatterns = [
	path("", views.index, name="index"),
	path("dogs", views.dogs, name="dogs"),
	path("cats", views.cats, name="cats"),
    path("about", views.about, name="about"),
    path("donation", views.donation, name="donation"),
    path("volunteer", views.volunteer, name="volunteer"),
    path("dogs/<int:dog_id>/", views.dog_info, name="dog_info"),
]
