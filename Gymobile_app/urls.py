from django.urls import path
from . import views

app_name='Gymobile_app'

urlpatterns = [
	path('', views.index, name='index'),
	path('days/', views.days, name='days'),
	path('days/(P<day_id>\d+)', views.day, name='day'),

	path('new_day/', views.new_day, name='new_day'),

	path('new_exercise/(P<day_id>\d+)', views.new_exercise, name='new_exercise'),

	path('edit_exercise/(P<workout_id>\d+)', views.edit_exercise, name='edit_exercise'),

	#adding a map route
	path('map/', views.map, name='map'),
]
