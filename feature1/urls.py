from django.urls import path
from feature1.views import *
app_name='something'
urlpatterns = [
    path('food/',food,name='food'),
]