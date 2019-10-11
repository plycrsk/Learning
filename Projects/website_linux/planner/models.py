from django.db import models
from datetime import date
from django.urls import reverse
# Create your models here.

class Appointment(models.Model):
	category 	= 	models.CharField(max_length = 25)
	#time 		=   models.TimeField(default='12:00')
	#date 		=   models.DateField()
	date_time   =   models.DateTimeField(null=True)
	#end_time    =   models.TimeField(default = '23:59')
	location 	=   models.CharField(max_length = 100)
	title 		=   models.CharField(max_length = 100, default = 'Appointment')
	
	def get_absolute_url(self):
		return reverse("planner:appointment_detail", kwargs={"appointment_id": self.id})
		#return f"/blog/detail/{self.id}"
	
	
#remember: always run python manage.py makemigrations and python manage.py migrate when making changes
#to models.py