from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from apicore import views as api_view
from django.conf import settings
from django.conf.urls.static import static
#from contact import urls

urlpatterns = [
	path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
	path('hello/', api_view.HelloView.as_view(), name='hello'),
	
	path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

	path('contact/', include('contacts.urls')),
	path('', include('userauth.urls'))

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

