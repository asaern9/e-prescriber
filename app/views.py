from django.shortcuts import render
from . forms import PrescriptionForm
# Create your views here.


def index(request):
    if request.method == 'POST':
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PrescriptionForm()
    return render(request, 'app/index.html', {'form': form})
