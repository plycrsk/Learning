from django.contrib import admin
from django.urls import path

from pages.views import planner_view

from planner.views import (
	appointment_create_view,
    appointment_list_view
)

app_name = 'planner'
urlpatterns = [
	  
    path('', appointment_list_view, name='planner'),
	path('appointment', appointment_create_view, name='appointment'),
]