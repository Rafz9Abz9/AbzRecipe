from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.recipes, name='recipes'),
    path('<int:recipe_id>', views.recipe_detail, name='recipe_detail'),
    path('delete-comment/<int:recipe_id>/<int:comment_id>',
         views.delete_comment, name='delete_comment'),
    path('like/<int:recipe_id>', views.like_recipe, name='like_recipe'),
    path('favorites', views.favorite_recipe, name='favorite'),

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
