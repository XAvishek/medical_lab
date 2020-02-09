from django.db import models

# Create your models here.

class TestCategory(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.CharField(max_length= 100)
    age = models.PositiveIntegerField()
    sex = models.CharField(max_length = 10)
    address = models.CharField(max_length= 200, default='')
    test_category = models.ManyToManyField(TestCategory, related_name='patient', blank=True)
    contact = models.IntegerField()
    collected_date = models.DateTimeField(auto_now_add=True)
    tested = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length= 100)
    contact = models.IntegerField()
    patient = models.ManyToManyField(Patient, related_name='doctor', blank=True)

    def __str__(self):
        return self.name


