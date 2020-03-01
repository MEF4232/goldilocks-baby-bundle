from django.shortcuts import render, get_object_or_404

from .models import Parent

def index(request):
	parents_list = Parent.objects.order_by('email_address')
	context = {
		'parents_list': parents_list,
	}
	return render(request, 'rentals/index.html', context)

def parentDetails(request, parent_id):
	parent = get_object_or_404(Parent, pk=parent_id)
	return render(request, 'rentals/parentDetails.html', {'parent': parent})
