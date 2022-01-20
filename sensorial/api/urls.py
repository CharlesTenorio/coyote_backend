from rest_framework.routers import SimpleRouter
from django.urls import path, include
from sensorial.api.viewsets import SensorViewSet, TemperatureViewSet, MoistureViewSet

routes = SimpleRouter()
routes.register(r'sensors', SensorViewSet)
routes.register(r'temperatures', TemperatureViewSet)
routes.register(r'moistures', MoistureViewSet)

urlpatterns = [
    path('v1/', include(routes.urls))
]
