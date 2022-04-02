from django.contrib import admin
from django.urls import path, include
from electric_trains import views
from electric_trains.views import TrainListView, TrainDetailView, TrainCreateView, TrainUpdateView, TrainDeleteView

urlpatterns = [
    # path('', views.electric_trains, name='home_electric_trains'),
    path('', TrainListView.as_view(), name='home_electric_trains'),
    path('detail/<int:pk>/', TrainDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', TrainUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', TrainDeleteView.as_view(), name='delete'),
    path('add/', TrainCreateView.as_view(), name='create'),
]