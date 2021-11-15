from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('getData/',views.getlastPoints),
    path('getOperations/',views.getOperations)

]
