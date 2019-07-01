from django.urls import path
from . import views

app_name='Gymobile_app'

urlpatterns = [
	path('', views.index, name='index'),
	path('days/', views.days, name='days'),
	path('days/(P<day_id>\d+)', views.day, name='day'),

	path('new_day/', views.new_day, name='new_day')
]
