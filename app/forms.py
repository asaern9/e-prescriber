from django import forms
from . models import Prescription


class DateInputM(forms.DateInput):
    input_type = 'date'


class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = '__all__'
        widgets = {
            'dosage': forms.Textarea(attrs={'class': 'form-control ', 'rows': 1, 'placeholder': 'Dosage'}),
            'precaution': forms.Textarea(attrs={'class': 'form-control ', 'rows': 1, 'placeholder': 'Precaution'}),
            'side_effect': forms.Textarea(attrs={'class': 'form-control', 'rows': 1, 'placeholder': 'Side effect'}),
            'drug_class': forms.TextInput(attrs={'class': 'form-control ', 'rows': 1, 'placeholder': 'Drug class'}),
            'drug_name': forms.TextInput(attrs={'class': 'form-control ', 'rows': 1, 'placeholder': 'Drug name'}),
            'drug_form': forms.Select(attrs={'class': 'form-control ', 'rows': 1, 'placeholder': 'Drug form'}),
            'channel': forms.Select(attrs={'class': 'form-control ', 'rows': 1, 'placeholder': 'Channel'}),
            'date_of_issue': DateInputM(attrs={'class': 'form-control ', 'rows': 1, 'placeholder': 'Date of issue'}),
            'end_date': DateInputM(attrs={'class': 'form-control ', 'rows': 1, 'placeholder': 'Date of issue'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control ', 'rows': 1, 'placeholder': 'Quantity'}),
            'administer_name': forms.TextInput(attrs={'class': 'form-control ', 'rows': 1, 'placeholder': 'Name'}),
            'administer_contact': forms.TextInput(attrs={'class': 'form-control ', 'rows': 1, 'placeholder': 'Phone'}),
            'name_of_pharmacy': forms.TextInput(attrs={'class': 'form-control ', 'rows': 1, 'placeholder': 'Pharmacy name'}),
            'pharmacy_address': forms.TextInput(attrs={'class': 'form-control ', 'rows': 1, 'placeholder': 'Pharmacy address'}),
            'patient_sex': forms.Select(attrs={'class': 'form-control ', 'rows': 1}),
            'patient_contact': forms.TextInput(attrs={'class': 'form-control ', 'rows': 1, 'placeholder': 'Phone'}),
            'patient_weight': forms.NumberInput(attrs={'class': 'form-control ', 'rows': 1, 'placeholder': 'Weight'}),
            'patient_date_of_birth': DateInputM(attrs={'class': 'form-control ', 'rows': 1, 'placeholder': 'DoB'}),
            'patient_age': forms.NumberInput(attrs={'class': 'form-control ', 'rows': 1, 'placeholder': 'Age'}),
            'patient_name': forms.TextInput(attrs={'class': 'form-control ', 'rows': 1, 'placeholder': 'Name'}),
            'postal_address': forms.TextInput(attrs={'class': 'form-control ', 'rows': 1, 'placeholder': 'Address'}),



        }
