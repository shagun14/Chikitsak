from django.urls import path , include
from . import views

urlpatterns = [
  path('get_feedback', views.get_feedback, name='get_feedback')
   
]