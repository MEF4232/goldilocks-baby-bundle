from django.contrib import admin

from .models import *

# TODO https://docs.djangoproject.com/en/3.0/intro/tutorial07/

class ParentAdmin(admin.ModelAdmin):
	list_display = ('id', 'first_name', 'last_name', 'email_address')
	search_fields = ['first_name', 'last_name', 'email_address']

admin.site.register(Parent, ParentAdmin)

class ItemAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')
	list_filter = ['size', 'season']
	search_fields = ['name']

admin.site.register(Item, ItemAdmin)

admin.site.register(ItemSize)
admin.site.register(ItemSeason)
