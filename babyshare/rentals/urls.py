from django.urls import path

from . import views

app_name = 'rentals'
urlpatterns = [
    path('', views.index, name='index'),
	path('parent/<int:parent_id>/', views.parentDetails, name='parentDetails'),
]