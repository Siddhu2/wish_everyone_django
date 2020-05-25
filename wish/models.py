from django.db import models

# Create your models here.
class wishlist(models.Model):
	wish_title = models.CharField(max_length=100)
	wish_description =models.TextField()
	pic = models.ImageField(upload_to='wish/images/')
