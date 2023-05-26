from django.urls import path, include
from rest_framework.authtoken.views import ObtainAuthToken
from . import views
app_name='api-v1'

urlpatterns = [
    #registration
    path('registration/' ,views.RegistrationApiView.as_view() , name = 'registration' ),
    path('token/login' , ObtainAuthToken.as_view(),name='token-login')
    #change password
    #reset password
    #login token
    #login jwt

]
