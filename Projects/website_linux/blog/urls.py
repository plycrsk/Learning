from django.contrib import admin
from django.urls import path

from pages.views import (
	blog_view,
	home_view
)

from blog.views import (
	blog_detail_view,
	blog_create_view,
	blog_delete_view,
	blog_list_view

)
app_name = 'blog'
urlpatterns = [
	  
    path('', blog_list_view, name='blog'),
    path('create/', blog_create_view, name='blog_create'),
    #path('blog_list', blog_list_view, name='blog_list'),
    path('<int:blog_id>/', blog_detail_view, name='blog_detail'),
    path('<int:blog_id>/delete/', blog_delete_view, name='blog_delete'),
	
]