from django.shortcuts import redirect, render
from .forms import MyForm
from .tasks import my_send_mail


def reminder(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            remind = form.cleaned_data['remind']
            date = form.cleaned_data['date']
            my_send_mail.apply_async((email, remind), eta=date)
            return redirect('reminder')
    else:
        form = MyForm()
    return render(request, 'reminder.html', {
        'form': form,
    })
