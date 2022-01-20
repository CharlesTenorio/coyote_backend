from rest_framework.routers import SimpleRouter
from django.urls import path, include
from app.api.viewsets import CompanyViewSet, AccommodationViewSet, ShedViewSet, SectorViewSet

routes = SimpleRouter()
routes.register(r'companies', CompanyViewSet)
routes.register(r'accommodations', AccommodationViewSet)
routes.register(r'sheds', ShedViewSet)
routes.register(r'sectors', SectorViewSet)

urlpatterns = [
    path('v1/', include(routes.urls))
]
