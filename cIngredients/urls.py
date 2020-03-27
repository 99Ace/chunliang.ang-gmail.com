from django.urls import path
from cIngredients.views import ingredients

urlpatterns = [
    path('', ingredients, name='ingredients'),
]