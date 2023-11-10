from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.recipes, name='recipes'),
    path('<int:recipe_id>', views.recipe_detail, name='recipe_detail'),
    path('like/<int:recipe_id>', views.like_recipe, name='like_recipe'),
   
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
