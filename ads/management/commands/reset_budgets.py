# ads/management/commands/reset_budgets.py
from django.core.management.base import BaseCommand
from ads.models.services.budget_service import BudgetService

class Command(BaseCommand):
    help = 'Reset daily and monthly budgets if needed'

    def handle(self, *args, **kwargs):
        BudgetService.reset_budgets()
        self.stdout.write(self.style.SUCCESS("Budgets successfully reset."))
