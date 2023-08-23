from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('save-entry/', views.save_entry, name='save_entry'),
]
