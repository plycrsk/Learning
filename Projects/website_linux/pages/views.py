from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
	print(request) #test line just to show what is being requested
	print(request.user) #prints request.user, which shows the user that is accessing site
	#return HttpResponse("<h1>Sam Kean</h1>") #string of HTML code
	return render(request, "home.html", {})

def blog_view(request, *args, **kwargs):
	my_context = {
		"my_text": "This is about us",
		"my_number": 123,
		"my_list": [123, 456, 78910, 'ABC']
		
	}
	return render(request, "blog.html", my_context)

def planner_view(request, *args, **kwargs):
	my_context = {
		"planner": "This is my planner"
	}
	return render(request, "planner.html", my_context)