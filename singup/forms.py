from django import forms 


class usersForms(forms.Form):
	name = forms.CharField(max_length=10, required=False, widget=forms.TextInput(attrs={'class' : 'form-control'}))
	lastname = forms.CharField(max_length=10, required=False, widget=forms.TextInput(attrs={'class' : 'form-control'}))
	username = forms.CharField(max_length=10, required=False, widget=forms.TextInput(attrs={'class' : 'form-control'}))
	email = forms.EmailField(label=u"mail", required=False, widget=forms.TextInput(attrs={'class' : 'form-control'}))
	password = forms.CharField(required=False, widget=forms.PasswordInput(attrs={'class' : 'form-control' , 'placeholder': 'Password' }))
	selfi = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class':'btn btn-default btn-file'}))

