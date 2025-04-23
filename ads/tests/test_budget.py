import pytest
from ads.models import Brand, Campaign
from ads.models.services.budget_service import BudgetService

@pytest.mark.django_db
def test_campaigns_are_paused_when_daily_budget_hit():
    brand = Brand.objects.create(name="BrandX", daily_budget=100, monthly_budget=1000)
    campaign = Campaign.objects.create(brand=brand, name="Test", active=True)

    BudgetService.check_and_update_spend(brand, 120)

    brand.refresh_from_db()
    campaign.refresh_from_db()
    assert not brand.active
    assert not campaign.active
