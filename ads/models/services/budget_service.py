from datetime import date, datetime
from django.utils.timezone import now
from ads.models import Brand, Campaign

class BudgetService:
    @staticmethod
    def check_and_update_spend(brand: Brand, spend_amount: float):
        brand.daily_spent += spend_amount
        brand.monthly_spent += spend_amount
        brand.save()
        BudgetService.apply_budget_rules(brand)

    @staticmethod
    def apply_budget_rules(brand: Brand):
        if brand.daily_spent >= brand.daily_budget or brand.monthly_spent >= brand.monthly_budget:
            brand.active = False
            brand.save()
            Campaign.objects.filter(brand=brand).update(active=False)

    @staticmethod
    def reset_budgets():
        today = date.today()
        for brand in Brand.objects.all():
            if brand.last_updated.month != today.month:
                brand.monthly_spent = 0
            if brand.last_updated != today:
                brand.daily_spent = 0
            brand.last_updated = today
            brand.active = True
            brand.save()
            Campaign.objects.filter(brand=brand).update(active=True)
