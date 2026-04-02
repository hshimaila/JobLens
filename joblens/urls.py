from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from analyzer.views import analyze_resume

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", analyze_resume, name="home"),
    path("analyze/", analyze_resume, name="analyze_resume"),
    path('api/', include('analyzer.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)