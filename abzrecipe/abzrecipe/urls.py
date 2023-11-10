from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from core.views import index, VerifivationView, contact, about

urlpatterns = [
    path('', index, name="home"),
    path('contact-us/', contact, name="contact"),
    path('about-us/', about, name="about"),
    path('auth/', include('core.urls')),
    path('recipes/', include('recipe.urls')),
    path('admin/', admin.site.urls),
    path('activate/<uidb64>/<token>', VerifivationView.as_view(), name='activate'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
