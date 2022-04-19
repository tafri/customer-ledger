from . import views
from django.urls import path

urlpatterns = [
    path('', views.account_details),
    path('<int:pk>', views.account_details)
]