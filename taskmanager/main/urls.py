from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.welcome),#welcome
    # path('sign_in/', TemplateView.as_view(template_name='main/sign_in.html'), views.sign_in),
    path('sign_in.html', views.sign_in),
    path('sign_up.html', views.sign_up),
    path('home_page.html', views.home_page),
    path('profile.html', views.profile),
    path('sign_in_email.html', views.sign_in_email),
    path('snippet.html', views.snippet),
    path('update_username.html', views.update_username),
    path('create.html', views.create)
]
