from django.contrib import admin
from django.urls import path,include
from app.views.data.home import home
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', home, name='home'),  # Home page
    path("app/", include("app.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)