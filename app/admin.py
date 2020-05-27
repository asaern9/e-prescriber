from django.contrib import admin
from .models import Prescription
# Register your models here.


class PrescriptionAdmin(admin.ModelAdmin):
    list_display =('patient_name', 'patient_contact', 'drug_name', 'quantity', 'administer_name')


admin.site.register(Prescription, PrescriptionAdmin)
