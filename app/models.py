from django.db import models

# Create your models here.
SEX = (
    ('MALE','MALE'),
    ('FEMALE', 'FEMALE')

)

DRUG_FORM = (
    ('CAPSULE', 'CAPSULE'),
    ('TABLET', 'TABLET'),
    ('OINTMENT', 'OINTMENT'),
    ('INJECTION', 'INJECTION')
)

CHANNEL = (
    ('ORAL', 'ORAL'),
    ('INTRAVENOUS', 'INTRAVENOUS')
)


class Prescription(models.Model):
    patient_name = models.CharField(max_length=150)
    patient_age = models.IntegerField()
    patient_sex = models.CharField(max_length=8, choices=SEX, default='MALE')
    patient_weight = models.FloatField(null=True)
    patient_contact = models.CharField(max_length=10)
    patient_date_of_birth = models.DateField(null=True)
    postal_address = models.CharField(max_length=150, null=True)
    drug_class = models.CharField(max_length=150, null=True)
    drug_name = models.CharField(max_length=150)
    drug_form = models.CharField(max_length=50, choices=DRUG_FORM, default='CAPSULE')
    channel = models.CharField(max_length=50, choices=CHANNEL, default='ORAL')
    quantity = models.IntegerField()
    dosage = models.TextField()
    precaution = models.TextField(null=True)
    side_effect = models.TextField(null=True)
    date_of_issue = models.DateField()
    end_date = models.DateField()
    administer_name = models.CharField(max_length=150)
    administer_contact = models.CharField(max_length=10)
    name_of_pharmacy = models.CharField(max_length=150)
    pharmacy_address = models.CharField(max_length=150)

    def __str__(self):
        return self.patient_name
