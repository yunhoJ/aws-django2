from django.urls import path
from boss import views

urlpatterns=[
    path('timeinput/<int:shop>',views.timeinput, name='timeinput')
]