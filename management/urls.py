from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegistrationView,EmailVerificationView,CustomObtainAuthToken,logout_view

urlpatterns = [
    path('registration/',RegistrationView.as_view(),name='registration'),
    path('verify-email/',EmailVerificationView.as_view(), name='verify-email'),
    path('login/',CustomObtainAuthToken.as_view(),name='login'),
    path('logout/',logout_view,name='logout'),
]
