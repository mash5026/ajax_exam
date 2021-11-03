from django.urls import path
from . import views

app_name = "ajax_app"

urlpatterns = [
    path('first/', views.index, name='index'),
]

