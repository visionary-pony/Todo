from django.contrib import admin
from django.contrib.auth import logout
from django.urls import path
from .views import home, login,signup , add_todo , signout,delete_todo,change_status
    
urlpatterns = [
    path('' ,home, name='home'),
    path('login/' , login,name = "login"),
    path('signup/', signup,name='signup'),
    path('add-todo/' , add_todo),
    path('logout/' , signout),
    path('delete-todo/<int:id>' , delete_todo),
    path('change-status/<int:id>/<str:status>' , change_status),
]
