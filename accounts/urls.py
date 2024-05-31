from django.urls import path

from .views import signup ,user_activate ,dashboard

urlpatterns = [
    path('signup' , signup ,name='signup'),
    path('<str:username>/activate',user_activate),


    path('dashboard' , dashboard),


]