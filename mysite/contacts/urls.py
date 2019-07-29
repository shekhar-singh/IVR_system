from userauth import views
from django.urls import path
from contacts import views
# SET THE NAMESPACE!
app_name = 'contacts'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[

    path('',views.home, name='home'),
	path('create/', views.create, name='create'),
	path('delete/<int:id>/', views.delete_contact, name='delete'),
	path('update/<int:id>/', views.update_contact, name='update_contact'),
	path('update_page/<int:id>/', views.update_page, name='update_page'),

]












