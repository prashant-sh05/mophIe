from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from hello_world.core import views as core_views  # Import core views
from .views import htop_view  # ✅ Ensure correct import

urlpatterns = [
    path("", core_views.index),  # Root path
    path("admin/", admin.site.urls),
    path("htop/", htop_view, name="htop"),  # ✅ Corrected view name
    path("_reload_/", include("django_browser_reload.urls")),
]

# Add static/media URLs if in DEBUG mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
