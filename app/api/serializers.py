from rest_framework.serializers import ModelSerializer
from app.models import Company, Accommodation, Shed, Sector



class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class AccommodationSerializer(ModelSerializer):
    class Meta:
        model = Accommodation
        fields = '__all__'


class ShedSerializer(ModelSerializer):
    class Meta:
        model = Shed
        fields = '__all__'


class SectorSerializer(ModelSerializer):
    class Meta:
        model = Sector
        fields = '__all__'

