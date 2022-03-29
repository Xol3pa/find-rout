from django.contrib import admin
from django.urls import path, include
from cities import views
from cities.views import CityDetailView, CityCreateView, CityUpdateView, CityDeleteView, CityListView

urlpatterns = [
    # path('', views.cities, name='home_cities'),
    path('', CityListView.as_view(), name='home_cities'),
    path('detail/<int:pk>/', CityDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', CityUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', CityDeleteView.as_view(), name='delete'),
    path('add/', CityCreateView.as_view(), name='create'),
]

