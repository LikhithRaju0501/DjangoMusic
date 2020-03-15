from django.urls import path
from music import views

urlpatterns = [

    path('',views.index,name="index")
]
