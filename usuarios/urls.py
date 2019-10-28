from django.urls import path, include
from .views import login


app_name = 'usuarios'

urlpatterns = [
    path('login/', login, name='login'),
]