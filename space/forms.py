from django import forms 


class post_forms(forms.Form):
	title = forms.CharField(max_length=20)
	aboutnow = forms.CharField(max_length=200)

