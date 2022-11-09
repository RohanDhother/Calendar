from django.urls import path, include

from racing_calendar import views, api

app_name = 'racing_calendar'
urlpatterns = [
#url paths to the view functions
path('', views.mainPage, name='mainPage'),
path('admin/', views.admin, name='admin'),

#paths to the api functions
path('api/Events/', api.Events_api, name='Events api'),
path('api/Allevents/', api.Allevents_api, name='Allevents api'),
path('api/DeleteEvent/', api.DeleteEvent_api, name='DeleteEvent api'),
path('api/AddEvent/', api.AddEvent_api, name='AddEvent api'),
]
