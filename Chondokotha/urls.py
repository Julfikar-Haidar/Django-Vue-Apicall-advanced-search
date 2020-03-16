
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="base"),
    path('api/data',views.data),
    path('api/districts',views.districts),
    path('api/kotha',views.kotha),

]
