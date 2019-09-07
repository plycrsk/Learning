from django import forms

from .models import BlogPost

class BlogPostForm(forms.ModelForm):
#this will overwrite the title field below
	title 		= forms.CharField(required=True, label = '',
								  widget=forms.TextInput(
									attrs={"placeholder": 'Blog Post Title'}
								  ))
	content     = forms.CharField(label = '',
								  widget=forms.Textarea(
											attrs={
												"placeholder": 'Blog Post Content',
												"class":"new-class-name two",
												"rows": 15,
												"id": 'my-id-for-text-area',
												#"cols": 15
												}))
	keywords    = forms.CharField(label = '',
								  #initial='Blog',
								  required=False,
								  widget=forms.TextInput(
									attrs={"placeholder": 'Keywords'}
								  ))
	class Meta:
		model = BlogPost
		fields = [
			'title',
			#'date',
			'content',
			'keywords'
			#'signature',
		]
	
	def clean_keywords(self, *args, **kwargs):
		keywords = self.cleaned_data.get("keywords")
		if ' ' not in keywords:
			return keywords
		else:
			raise forms.ValidationError("Please separate keywords with a ','")
		
class RawBlogPostForm(forms.Form):
#Must declare inputs when using standard django Form, rather than ModelForm
	title 		= forms.CharField(required=True,
								  widget=forms.TextInput(
									attrs={"placeholder": 'Blog Post Title'}
								  ))
	#standard default required = True, so only need if false
	content     = forms.CharField(widget=forms.Textarea(
											attrs={
												"class":"new-class-name two",
												"rows": 20,
												"id": 'my-id-for-text-area',
												"cols": 15
												}))
	keywords    = forms.CharField(initial='Blog',required=False)
	
