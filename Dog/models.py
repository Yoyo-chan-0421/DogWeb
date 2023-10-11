from django.db import models

# Create your models here.

class Dogs(models.Model):
	name = models.CharField(max_length=100)
	image = models.ImageField(upload_to="media/")
	bio = models.TextField()

	def __str__(self):
		return self.name
class Cats(models.Model):
	name = models.CharField(max_length=100)
	image = models.ImageField(upload_to="media/")
	bio = models.TextField()