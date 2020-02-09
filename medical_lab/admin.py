from django.contrib import admin
from medical_lab.models import Doctor, Patient, TestCategory

# Register your models here.

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(TestCategory)
