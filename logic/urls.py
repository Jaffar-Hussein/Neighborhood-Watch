from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('auth/login', views.login_request, name='login'),
    path('auth/register', views.register, name='register'),
    path('auth/logout', views.logout_request, name='logout'),
    path('account', views.account, name='account'),
    path('business', views.Business_request, name='business')
]
