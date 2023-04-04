from django import forms

class UrlForm(forms.Form):
    url = forms.CharField(label='ORACLE URL:', max_length=100)