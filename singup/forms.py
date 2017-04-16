from django import forms 


class usersForms(forms.Form):
	name = forms.CharField(max_length=10, required=False)
	lastname = forms.CharField(max_length=10, required=False)
	username = forms.CharField(max_length=10, required=False)
	email = forms.EmailField(label=u"mail", required=False)
	password = forms.CharField(widget=forms.PasswordInput, required=False)
	selfi = forms.ImageField(required=False)

