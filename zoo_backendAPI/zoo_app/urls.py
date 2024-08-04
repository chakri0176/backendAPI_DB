# zoo_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home view
    path('species_info', views.handle_species_info, name='handle_species_info'),
    path('species_info/<str:id>', views.handle_species_info_detail, name='handle_species_info_detail'),
    path('animal_info', views.handle_animal_info, name='handle_animal_info'),
    path('animal_info/<str:id>', views.handle_animal_info_detail, name='handle_animal_info_detail'),
    path('animal_feeding', views.handle_animal_feeding, name='handle_animal_feeding'),
    path('animal_feeding/<str:id>', views.handle_animal_feeding_detail, name='handle_animal_feeding_detail'),
    path('animal_health', views.handle_animal_health, name='handle_animal_health'),
    path('animal_health/<str:id>', views.handle_animal_health_detail, name='handle_animal_health_detail'),
    path('enclosure_info', views.handle_enclosure_info, name='handle_enclosure_info'),
    path('enclosure_info/<str:id>', views.handle_enclosure_info_detail, name='handle_enclosure_info_detail'),
]
