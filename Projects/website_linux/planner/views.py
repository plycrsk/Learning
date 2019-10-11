from django.shortcuts import render, redirect

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
		form = AppointmentForm()
		return redirect("../")
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

def appointment_detail_view(request, appointment_id):
	try:
		obj = Appointment.objects.get(id=appointment_id)
	except Appointment.DoesNotExist:
		raise Http404
	context = {
		'object':obj
	}
	return render(request, "Appointment_detail.html", context)
	