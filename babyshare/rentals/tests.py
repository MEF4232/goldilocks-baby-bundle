from django.test import TestCase

from .models import *

###############################################################################
# USERS
###############################################################################

class ParentModelTests(TestCase):
	
	def test_unique_email_address(self):
		""" Each parent must have a unique email address """
		p1 = Parent(first_name = 'Joe', last_name = 'Smith', email_address = 'test@gmail.com')
		
		try:
			p2 = Parent(first_name = 'Jane', last_name = 'Doe', email_address = 'test@gmail.com')
		except:
			# https://docs.python.org/3/library/unittest.mock.html
			# https://stackoverflow.com/questions/27813027/django-python-unittesting-how-to-force-exception-of-try-except-block
			pass

class ChildTests(TestCase):

	def test_nothing(self):
		pass


###############################################################################
# ITEMS
###############################################################################


class ItemModelTests(TestCase):

	def test_nothing(self):
		pass
		
class ItemSizeModelTests(TestCase):

	def test_nothing(self):
		pass
		
class ItemSeasonModelTests(TestCase):

	def test_nothing(self):
		pass

class ItemCategoryModelTests(TestCase):

	def test_nothing(self):
		pass