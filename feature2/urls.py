from django.urls import path
from feature2.views import *
app_name='something'
urlpatterns = [
    path('mobile/',mobile,name='mobile'),
]