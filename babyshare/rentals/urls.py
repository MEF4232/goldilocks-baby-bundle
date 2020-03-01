from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
	path('parent/<int:parent_id>/', views.parentDetails, name='parentDetails'),
]