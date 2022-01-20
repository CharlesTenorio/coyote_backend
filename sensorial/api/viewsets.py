from rest_framework.viewsets import ModelViewSet
from sensorial.models import Sensor, Temperature, Moisture
from sensorial.api.serializers import SensorSerializer, TemperatureSerializer, MoistureSerializer


class SensorViewSet(ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class TemperatureViewSet(ModelViewSet):
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer

class MoistureViewSet(ModelViewSet):
    queryset = Moisture.objects.all()
    serializer_class = MoistureSerializer
