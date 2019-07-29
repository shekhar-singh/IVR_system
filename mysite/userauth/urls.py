#from django.conf.urls import url
from userauth import views
from django.urls import path
from userauth import views
# SET THE NAMESPACE!
app_name = 'userauth'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    path('register/',views.register, name='register'),
    path('user_login/',views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='logout'),
    path('',views.index, name='index'),
    path('special/', views.special, name='special')
    
]
