from django.urls import path
from . import views

urlpatterns = [
    path('',views.loginPage,name='login-page' ),
    path('register/',views.registerPage,name='register-page' ),
    path('logout/',views.logout,name='logout' ),
]