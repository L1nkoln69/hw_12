from django.shortcuts import redirect, render, get_object_or_404
from .forms import MyForm
from .tasks import my_send_mail
from .models import Author, Quotes


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


def authors(request):
    author = Author.objects.all()
    return render(request, 'author.html', {'author': author})


def authors_info(request, pk):
    author_info = get_object_or_404(Author.objects.all(), pk=pk)
    return render(request, 'author_info.html', {'author_info': author_info})


def quote(request):
    quotes = Quotes.objects.all()
    return render(request, 'quotes.html', {'quotes': quotes})
