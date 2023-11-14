from django.urls import path
from . import views

urlpatterns = [
	path("", views.index, name="index"),
	path("狗狗班", views.dogs, name="dogs"),
	path("貓貓班", views.cats, name="cats"),
    path("關於我們", views.about, name="about"),
    path("支持我們的生活費", views.donation, name="donation"),
    path("地址", views.volunteer, name="volunteer")
]
