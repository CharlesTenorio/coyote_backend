from django.urls import path, include

urlpatterns = [
    path('', include('api.docs.urls')),
    path('', include('app.api.urls')),
    path('', include('sensorial.api.urls'))
]
