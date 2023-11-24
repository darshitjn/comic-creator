from django.urls import path
from .views import generate_comics

urlpatterns = [
    path('generate-comics/', generate_comics, name='generate_comics'),
]