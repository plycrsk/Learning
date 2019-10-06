from django.db import models
from datetime import date
from django.urls import reverse

# Create your models here.
class BlogPost(models.Model):
	title      = models.CharField(max_length = 50) # max_length = required
	date       = models.DateField(default=date.today)
	content    = models.TextField(blank = True, null = True)
	keywords   = models.TextField(blank = True, null = True)
	signature  = models.TextField(default='Sam Kean')
	
	def get_absolute_url(self):
		return reverse("blog:blog_detail", kwargs={"blog_id": self.id})
		#return f"/blog/detail/{self.id}"
	
