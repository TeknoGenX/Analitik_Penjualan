from django.shortcuts import render
from .forms import ContactForm

def contact_page(request):
    form = ContactForm()
    return render(request, 'contact/index.html', {'form': form})
