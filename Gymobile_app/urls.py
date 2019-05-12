from django.urls import path
from . import views

app_name='Gymobile_app'
urlpatterns = [
	path('', views.index, name='index'),
]
