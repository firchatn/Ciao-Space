from django import forms 


class post_forms(forms.Form):
	title = forms.CharField(max_length=20)
	aboutnow = forms.CharField(max_length=200)

class message_forms(forms.Form):
	msg = forms.CharField(max_length=2000)