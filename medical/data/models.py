from django.db import models

# Create your models here.

class Patient(models.Model):
    name = models.CharField(max_length=260)
    causes = models.TextField()
    symptoms = models.TextField()
    diagnoses = models.TextField()
    treatment = models.TextField()

    def __str__(self):
        return self.name