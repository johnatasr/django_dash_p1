from django.urls import path, include
from .views import painel_monitoramento

app_name = 'mediar'

urlpatterns = [
    path('monitoramento/', painel_monitoramento, name='monitoramento')
]