import datetime

from django import forms


class MyForm(forms.Form):
    email = forms.EmailField(label='email')
    date = forms.DateTimeField(label='время на которое нужно запланировать', initial=datetime.datetime.now())
    remind = forms.CharField(widget=forms.Textarea)
