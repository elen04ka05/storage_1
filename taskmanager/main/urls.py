from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('sign_in', views.sign_in, name='sign_in'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('home', views.home, name='home'),
    path('snippet/<int:id>', views.snippet, name='snippet'),
    path('snippet/<int:id>/history', views.history, name='history'),
]
