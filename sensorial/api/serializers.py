from rest_framework.serializers import ModelSerializer
from sensorial.models import Sensor, Temperature, Moisture


class SensorSerializer(ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'


class TemperatureSerializer(ModelSerializer):
    class Meta:
        model = Temperature
        fields = '__all__'


class MoistureSerializer(ModelSerializer):
    class Meta:
        model = Moisture
        fields = '__all__'

