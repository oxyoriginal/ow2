from django.urls import path
from ow_app.views import base

urlpatterns = [
    path('', base, name='base'),
]