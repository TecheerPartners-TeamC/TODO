from django.urls import path
from . import views

urlpatterns = [
    path('task/', views.all),
    path('incomplete/', views.incom),
    path('complete/', views.com),
    path('POST/', views.create),
    path('DELETE/<int:pk>/', views.delete),
    path('PUT/<int:pk>/', views.update),
]