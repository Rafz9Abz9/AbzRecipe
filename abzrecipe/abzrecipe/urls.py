from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from core.views import index, VerifivationView

urlpatterns = [
    path('', index, name="home"),
    path('auth/', include('core.urls')),
    path('admin/', admin.site.urls),
    path('activate/<uidb64>/<token>', VerifivationView.as_view(), name='activate'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
