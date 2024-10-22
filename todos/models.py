from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255, null=True, blank=True)  
    extracted_date = models.DateField(null=True, blank=True)
    extracted_time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return self.title