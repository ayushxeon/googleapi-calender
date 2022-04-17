from django.urls import path

from . import views

urlpatterns=[
    path('init/',views.login_view,name='login'),
    path('logout/',views.revoke,name='logout'),
    path('callback/',views.redirected_callback,name='redirected'),

]