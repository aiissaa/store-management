from django.urls import path

from . import views

app_name = 'customer'

urlpatterns = [
    path('register/', views.SignUpView.as_view(), name='register'),
]