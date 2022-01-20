from rest_framework import permissions
from drf_yasg2.views import get_schema_view
from drf_yasg2 import openapi


schema_view = get_schema_view(
  openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Seus problemas acabaram.",
      terms_of_service="https://joaofilho.dev/",
      contact=openapi.Contact(email="devdrummerzzz@gmail.com"),
      license=openapi.License(name="Copyright License"),    
    ),
  public=True,
  permission_classes=(permissions.AllowAny,),
)