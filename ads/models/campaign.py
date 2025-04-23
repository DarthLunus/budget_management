from django.db import models

class Campaign(models.Model):
    # Definição dos campos da Campaign
    name = models.CharField(max_length=255)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    dayparting_start = models.TimeField(null=True, blank=True)
    dayparting_end = models.TimeField(null=True, blank=True)

    def __str__(self):
        return self.name
