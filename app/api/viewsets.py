from rest_framework.viewsets import ModelViewSet
from app.models import Company, Accommodation, Shed, Sector
from app.api.serializers import CompanySerializer, AccommodationSerializer, ShedSerializer, SectorSerializer


class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class AccommodationViewSet(ModelViewSet):
    queryset = Accommodation.objects.all()
    serializer_class = AccommodationSerializer

class ShedViewSet(ModelViewSet):
    queryset = Shed.objects.all()
    serializer_class = ShedSerializer

class SectorViewSet(ModelViewSet):
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer
