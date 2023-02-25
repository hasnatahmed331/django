from django.urls import path
from . import views

urlpatterns = [
    path('azure-ad/login/', views.azure_ad_b2c_login, name='azure_ad_b2c_login'),
    path('azure-ad/callback/', views.azure_ad_b2c_callback, name='azure_ad_b2c_callback'),
]