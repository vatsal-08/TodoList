from django.urls import path
from accounts.views import *
from django.contrib.auth.views import LoginView
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', logout, name='logout'),
]
