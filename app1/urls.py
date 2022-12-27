from django.urls import path
from app1.views import *
app_name='something1'
urlpatterns=[
    path('naveen/',naveen,name='naveen'),
    path('sekhar/',sekhar,name='sekhar'),
]