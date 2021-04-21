import psycopg2 
from django.urls import path

from .import views

urlpatterns = [
    path('',views.home, name='home'),
    path('add_todo',  views.add_todo),
    path('delete_todo/<int:todo_id>/',views.delete_todo),
    path('login/',views.login, name='login'),
    path('new/',views.new, name='new.html')



] 