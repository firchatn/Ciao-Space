from django import forms


class post_forms(forms.Form):
    title = forms.CharField(max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    aboutnow = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control'}))


class message_forms(forms.Form):
    msg = forms.CharField(max_length=2000, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
