from django.db import models

class Parent(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	email_address = models.EmailField(unique = True)
	
	def __str__(self):
		return f'{self.first_name} {self.last_name}, {self.email_address}'