from django.urls import path
from order import views

urlpatterns=[
    path('shops/',views.shop,name="shop"),
    path('menus/',views.menu, name="menu"),
]