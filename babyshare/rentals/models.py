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
	category = models.ForeignKey('ItemCategory', help_text='Select the category of the item.', on_delete=models.PROTECT, null=True)
	
	SUBCAT_LEN = (
		('n', 'Not Applicable'),
		('s', 'Short'),
		('l', 'Long'),
	)
	SUBCAT_W = (
		('n', 'Not Applicable'),
		('h', 'Heavy'),
		('l', 'Light'),
	)
	
	subcategory_length = models.CharField(max_length=1, choices=SUBCAT_LEN, default='n', help_text='Choose whether item is long or short. (e.g. jeans are long, t-shirts are short, hats are Not Applicable)', verbose_name='Item Length')
	subcategory_weight = models.CharField(max_length=1, choices=SUBCAT_W, default='n', help_text='Choose whether item is heavy or light. (e.g. winter jackets are heavy, t-shirts are light)', verbose_name='Item Weight')
	
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

class ItemCategory(models.Model):
	name = models.CharField(max_length=200, help_text='Enter a category (e.g. Shirts).')
	
	def __str__(self):
		return self.name