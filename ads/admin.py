from django.contrib import admin
from ads.models.brand import Brand
from ads.models.campaign import Campaign

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'daily_budget', 'monthly_budget', 'daily_spent', 'monthly_spent', 'active')
    search_fields = ('name',)

@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'active', 'dayparting_start', 'dayparting_end')
    list_filter = ('active', 'brand')
    search_fields = ('name',)
