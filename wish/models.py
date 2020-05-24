from django.db import models

# Create your models here.
class wishlist(models.Model):
	wish_title = models.CharField(max_length=100)
	wish_description =models.CharField(max_length=300)
	pic = models.ImageField(upload_to='wish/images/')
