from django.db import models

class Parent(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	email_address = models.EmailField(unique = True)
	
	def __str__(self):
		return f'{self.first_name} {self.last_name}'
		
class Item(models.Model):
	name = models.CharField(max_length=200)
	size = models.ForeignKey('ItemSize', help_text='Select the size of the item.', on_delete=models.PROTECT, null=True)
	season = models.ManyToManyField('ItemSeason', help_text='Select all relevant seasons.')
	#category = models.ManyToManyField(ItemCategory)
	
	def __str__(self):
		return self.name

class ItemSize(models.Model):
	name = models.CharField(max_length=200, help_text='Enter an item size.')
	
	def __str__(self):
		return self.name

class ItemSeason(models.Model):
	name = models.CharField(max_length=200, help_text='Enter a season or holiday (e.g. Spring, Christmas).')
	
	def __str__(self):
		return self.name