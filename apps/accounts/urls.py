from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('auth/', include('allauth.urls')),
]