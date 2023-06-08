from django.urls import path, include
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from .. import views


urlpatterns = [
    #registration
    path('registration/' ,views.RegistrationApiView.as_view() , name = 'registration' ),
    
    path('test-email' , views.TestEmailSend.as_view() , name = 'test-email'),
    #activation
    # path('activation/confirm/')

    #resend activation
    # path('activation/resend/')
    
    
    
    #change password
    path("change-password/",views.ChangePasswordApiView.as_view(),name="change-password"),
    #reset password
    #login and logout token
    path('token/login/' , views.CustomObtainAuthToken.as_view(),name='token-login'),
    path('token/loout/' , views.CustomDiscardAuthToken.as_view(),name='token-logout'),
    
    #login jwt
    path('jwt/create/',views.CustomTokenObtainPairView.as_view(),name = 'jwt-create'),
    path('jwt/refresh/',TokenRefreshView.as_view() , name = 'jwt-refresh'),
    path('jwt/verify/' , TokenVerifyView.as_view() , name='jwt-verfy'),
]