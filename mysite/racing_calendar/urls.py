from django.urls import path, include

from racing_calendar import views, api

app_name = 'racing_calendar'
urlpatterns = [
#url paths to the view function
path('', views.mainPage, name='mainPage'),
path('admin/', views.admin, name='admin'),
]
