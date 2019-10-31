from django.urls import path, include
from .views import home, painel, usa_painel
from portal.dash_apps.finished_apps import dahsboard1

app_name = 'portal'

urlpatterns = [
    path('', home, name='home'),
    path('painel/', painel, name='painel'),
    path('mapa/', usa_painel, name='usa'),
]