from django.shortcuts import render
from .forms import MyForm


def reminder(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            return render(request, 'reminder.html', {
                'form': form
            })
    else:
        form = MyForm()
    return render(request, 'reminder.html', {
        'form': form,
    })
