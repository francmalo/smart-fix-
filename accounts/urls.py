from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name="login_view"),
    path('register', views.register_view, name="registration_view"),
    path('technician',views.technician_signup,name="technician_signup"),
    path('logout',views.logout_view,name="logout_view")
]
