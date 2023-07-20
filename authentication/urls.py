from . import views
from django.urls import path


app_name = 'authentication'

urlpatterns = [
    path("signup/", views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
]