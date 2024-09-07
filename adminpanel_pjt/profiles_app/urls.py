from django.urls import path
from . import views

urlpatterns = [
    path('userHome/',views.userHomePage,name='user-home' ),
    path('adminPage/',views.adminHomePage,name='admin-home' ),

    path('edit/<int:id>/',views.edit,name='edit' ),
    path('delete-user/<int:id>/',views.deleteUser,name='delete-user' ),

    path('add/',views.addUsers,name='add-users' ),


    path('sample/',views.sampleView,)

]