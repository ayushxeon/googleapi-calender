from django.urls import path

from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('rest/v1/calendar/redirect/',views.get_calender_event_list,name='events'),
]