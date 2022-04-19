from . import views
from django.urls import path

urlpatterns = [
    path('', views.user_details),
    path('<int:pk>', views.user_details)
]