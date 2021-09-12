from django.urls import path
from .views import *

urlpatterns = [
    path('', to_do),
    path('to_do', to_do),
    path('delete/<int:id1>', delete),
    path('edit/<int:id2>', edit),
]
