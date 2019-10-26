from django.urls import path, include
from .views import home
from portal.dash_apps.finished_apps import dahsboard1

app_name = 'portal'

urlpatterns = [
    path('', home, name='home'),
]