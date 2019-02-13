from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Book(models.Model):
	seller = models.ForeignKey(User, default = 1 , on_delete = models.CASCADE)
	name=models.CharField(max_length=100)
	image=models.ImageField(null=True, blank=True)
	condition=models.CharField(max_length=50)
	isbn=models.CharField(max_length=100)
	author=models.CharField(max_length=60)

	def __str__(self):
		return self.name

class Cart(models.Model):
	book= models.ForeignKey(Book, on_delete = models.CASCADE)
	user = models.ForeignKey(User ,on_delete = models.CASCADE)
	




		