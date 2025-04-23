from rest_framework import serializers
from ads.models.brand import Brand
from ads.models.campaign import Campaign

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class CampaignSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()

    class Meta:
        model = Campaign
        fields = '__all__'
