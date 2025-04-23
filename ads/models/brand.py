from django.db import models
from django.utils.timezone import now

class Brand(models.Model):
    name = models.CharField(max_length=100)
    daily_budget = models.DecimalField(max_digits=10, decimal_places=2)
    monthly_budget = models.DecimalField(max_digits=12, decimal_places=2)
    daily_spent = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    monthly_spent = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    active = models.BooleanField(default=True)
    last_updated = models.DateField(default=now)

    def __str__(self):
        return self.name
