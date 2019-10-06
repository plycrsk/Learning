from django.shortcuts import render

from .forms import AppointmentForm
from .models import Appointment

# Create your views here.
def appointment_create_view(request):
	initial_data = {
		'title': 'My title'
	}
	#used to edit model form data
	#obj = BlogPost.objects.get(id=1)
	form = AppointmentForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = Appointment_Form()
	context = {
		'form':form
	}
	return render(request, "Appointment_create.html", context)

def appointment_list_view(request):
	queryset = Appointment.objects.all() #list of blog post titles
	context = {
		"object_list": queryset
	}
	return render(request, "Appointment_list.html", context)