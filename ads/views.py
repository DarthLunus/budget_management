from rest_framework import viewsets
from ads.models.brand import Brand
from ads.models.campaign import Campaign
from ads.serializers import BrandSerializer, CampaignSerializer

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
