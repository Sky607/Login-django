from django.urls import path
from basic_app import views

# SET THE NAMESPACE!
app_name = 'basic_app'

# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    path('special/index/',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('user/',views.user_login,name='user'),
    path('logout/special/',views.special,name='special'),
    
]
