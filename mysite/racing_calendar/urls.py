from django.urls import path, include

from racing_calendar import views, api

app_name = 'racing_calendar'
urlpatterns = [
#url paths to the view functions
path('', views.mainPage, name='mainPage'),
path('admin/', views.admin, name='admin'),

#paths to the api functions
path('api/events/', api.events_api, name='events api'),
]
