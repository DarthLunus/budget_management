from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ads.views import BrandViewSet, CampaignViewSet

router = DefaultRouter()
router.register(r'brands', BrandViewSet)
router.register(r'campaigns', CampaignViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
