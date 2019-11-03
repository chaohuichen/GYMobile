from django.contrib import admin

# Register your models here.
from Gymobile_app.models import WorkoutLog,Exercies,Routine

admin.site.register(Routine)
admin.site.register(WorkoutLog)
admin.site.register(Exercies)
