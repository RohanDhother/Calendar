from django.urls import path, include

from racing_calendar import views, api

app_name = 'racing_calendar'
urlpatterns = [
path('', views.mainPage, name='mainPage'),
path('admin/', views.admin, name='admin'),
]
