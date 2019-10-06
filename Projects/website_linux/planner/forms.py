from django import forms
from django.contrib.admin.widgets import AdminDateWidget

from .models import Appointment

class AppointmentForm(forms.ModelForm):
#this will overwrite the title field below
	title 		= forms.CharField(required=True, label = '',
								  widget=forms.TextInput(
									attrs={"placeholder": 'Appointment'}
								  ))
	category     = forms.CharField(required=True, label = '',
								  widget=forms.TextInput(
									attrs={"placeholder": 'Category'}
								  ))
	location    = forms.CharField(required=True, label = '',
								  widget=forms.TextInput(
									attrs={"placeholder": 'Where?'}
								  ))
	date_time    = forms.DateTimeField(required=True, label = '', 
								  widget=AdminDateWidget(
									attrs={"placeholder": 'Date/Time?'}
								  ))
	
	class Meta:
		model = Appointment
		fields = [
			'title',
			'category',
			'location',
			'date_time',
		]