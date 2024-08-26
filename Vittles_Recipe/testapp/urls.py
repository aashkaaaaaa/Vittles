from django.urls import path


from . import views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


# URL Conf
urlpatterns = [
    path('vittlesin/', views.ingredient_form_view, name='vittles in'),
    path('vittlesout/', views.recipes_view, name='vittles out'),
    path('recipes/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('llamaout/', views.recipe_recommend_llama, name='llama output')
]
