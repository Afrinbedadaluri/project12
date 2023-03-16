from django.urls import path
from app2.views import *
app_name='birds'
urlpatterns=[
    path('birds/',birds,name='birds'),
]