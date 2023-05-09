from django.urls import path

from .import views

from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view


schema_view = swagger_get_schema_view(
    openapi.Info(
        title="TicketWeb API",
        default_version='1.0.0',
        description="API documentation of App",
    ),
    public=True,
)


urlpatterns = [
    path('swagger/schema/', schema_view.with_ui('swagger', cache_timeout=0), name="swagger-schema"),
    path('tickets/<int:ticket_id>/qr_code/', views.generate_qr_code, name='generate_qr_code'),
]

