from django.contrib import admin
from django.urls import path, include
from mots.views import enrichir_mot
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('mots.urls')),
]


from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api/auth/token/', obtain_auth_token, name='api_token_auth'),
    path('enrichir-mot/', enrichir_mot, name="enrichir-mot"),
]
urlpatterns = [
    path('api/enrichir-mot/', enrichir_mot, name="enrichir-mot"),
]