from django.urls import path
from . import views

urlpatterns = [
    path('', views.library_home),
    path('books/', views.library_books)
]
