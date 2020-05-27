from django.contrib import messages
from django.shortcuts import render, redirect
from . forms import PrescriptionForm
# Create your views here.


def index(request):
    if request.method == "POST":
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            form_save = form.save()
            messages.success(request, 'News submitted for approval')
            return redirect('index')
    else:
        form = PrescriptionForm()
    return render(request, 'app/index.html', {'form': form})
