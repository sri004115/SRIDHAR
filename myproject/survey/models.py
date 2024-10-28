from django.db import models

class Survey(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=10)
    health_condition = models.TextField()
    
    def __str__(self):
        return self.name
