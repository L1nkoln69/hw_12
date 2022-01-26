import datetime
from django.utils import timezone
from django import forms


class MyForm(forms.Form):
    email = forms.EmailField(label='email')
    date = forms.DateTimeField(label='время на которое нужно запланировать',
                               initial=timezone.now() + datetime.timedelta(hours=2))
    remind = forms.CharField(widget=forms.Textarea)

    def clean_date(self):
        date = self.cleaned_data.get('date')
        if date < timezone.now():
            raise forms.ValidationError('нельзя делать напоминание на прошлое')
        elif date > timezone.now() + datetime.timedelta(days=2):
            raise forms.ValidationError('нельзя делать напоминание больше чем на 2 дня')
        else:
            return date
