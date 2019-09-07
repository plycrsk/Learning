from django.db import models
from datetime import date

# Create your models here.
class BlogPost(models.Model):
	title      = models.CharField(max_length = 50) # max_length = required
	date       = models.DateField(default=date.today)
	content    = models.TextField(blank = True, null = True)
	keywords   = models.TextField(blank = True, null = True)
	signature  = models.TextField(default='Sam Kean')
	
	
	
