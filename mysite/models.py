from django.db import models

# Create your models here.


class Student(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)

	def _str_(self):
		return self.first_name

	
class Contact(models.Model):
	Email = models.EmailField()
	Subject = models.CharField(max_length=100)
	Message = models.TextField()
	
	def _str_(self):
		return self.Email
	
		