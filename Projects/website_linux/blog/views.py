from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .forms import BlogPostForm, RawBlogPostForm
from .models import BlogPost

def blog_create_view(request):
	initial_data = {
		'title': 'My title'
	}
	#used to edit model form data
	#obj = BlogPost.objects.get(id=1)
	form = BlogPostForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = BlogPostForm()
	context = {
		'form':form
	}
	return render(request, "BlogPost_create.html", context)


def blog_detail_view(request, blog_id):
	#obj = BlogPost.objects.get(id=blog_id)
	#obj = get_object_or_404(BlogPost, id=blog_id)
	try:
		obj = BlogPost.objects.get(id=blog_id)
	except BlogPost.DoesNotExist:
		raise Http404
	context = {
		'object':obj
	}
	return render(request, "BlogPost_detail.html", context)


# # Create your views here.
# def blog_create_view(request):
# 	my_form = RawBlogPostForm()
# 	if request.method == 'POST':
# 		my_form = RawBlogPostForm(request.POST)
# 		if my_form.is_valid():
# 			print(my_form.cleaned_data)
# 			BlogPost.objects.create(**my_form.cleaned_data)
# 		else:
# 			print(my_form.errors)
# 	context = {
# 		"form": my_form
# 	}
# 	return render(request, "BlogPost_create.html", context)

# def blog_create_view(request):
# 	# print(request.GET['title'])
# 	# print(request.POST)
# 	my_new_title = request.POST.get('title')
# 	if my_new_title != None:
# 		print(my_new_title)
# 	# print(my_new_title) if my_new_title != 'None'
# 	context = {}
# 	return render(request, "BlogPost_create.html", context)
#


