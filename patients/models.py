# patients/models.py
from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    height = models.FloatField(help_text="Height in cm")
    weight = models.FloatField(help_text="Weight in kg")
    age = models.IntegerField()
    bp_level = models.CharField(max_length=20, verbose_name="BP Level (e.g., 120/80)")
    created_at = models.DateTimeField(auto_now_add=True)

    def __clstr__(self):
        return self.name
