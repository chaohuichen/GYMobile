from django.urls import path
from . import views

app_name='Gymobile_app'

urlpatterns = [
	#homepage
	path('', views.index,name='index'),

	#workoutlogs page#
	path('workoutlogs/', views.workoutlogs, name='workoutlogs'),

	path('workouts/(P<workoutlog_id>\d+)', views.workoutlog, name='workoutlog'),

	path('new_log/', views.new_log, name='new_log'),

	path('new_exercise/(P<day_id>\d+)', views.new_exercise, name='new_exercise'),

	path('edit_exercise/(P<workout_id>\d+)', views.edit_exercise, name='edit_exercise'),
	#adding a map route
	path('map/', views.map, name='map'),

]
