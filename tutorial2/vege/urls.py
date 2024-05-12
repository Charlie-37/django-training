
from django.urls import path
from .views import *

urlpatterns = [
    path('add_receipes/',receipes ,name='receipes'),
    path('login/',login_page ,name='login'),
    path('logout/',logout_page ,name='logout'),
    path('register/',register_page ,name='register'),
    path('student/',student_page ,name='student'),
    path('student_data/',student_view_page,name='student_view'),
    path('update_receipe/<int:id>',update_receipe ,name='update_receipe'),
    path('delete_receipe/<int:id>',delete_receipe ,name='delete_receipe'),
]
