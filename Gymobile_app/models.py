from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import date

# Create your models here.

class WorkoutLog(models.Model):
    #day = models.DateTimeField(default=datetime.now()+timedelta(days=30))
    day = models.PositiveIntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    #routine = models.ForeignKey(Routine,on_delete=models.CASCADE)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        "..return"
        return '%s' % date(self.date_added,"n/j/Y")

class Routine(models.Model):
    """docstring for WorkoutLog."""
    RoutineName = models.CharField(max_length = 30)
    WorkoutLog=models.ForeignKey(WorkoutLog,on_delete=models.CASCADE)
    #Exercies = models.ForeignKey(Exercies, on_delete=models.CASCADE)

    def __str__(self):
        return 'Routine '+str(self.RoutineName)


class Exercise(models.Model):
    "workout type"
    Back='Back Exercies'
    Leg='Legs Exercies'
    Shoulder='Shoulder Exercies'
    Chest='Chest Exercies'
    type_of_workout=[
    (Back,'Back'),
    (Leg,'Leg'),
    (Shoulder,'Shoulder'),
    (Chest,'Chest'),
    ]

    workoutlog = models.ForeignKey(WorkoutLog,on_delete=models.CASCADE)
    category = models.CharField(
    max_length = 15
    )
    bodypart = models.CharField(
        max_length=15,
        choices=type_of_workout,
        default=Back,)
    date_added = models.DateTimeField(auto_now_add=True)
    description = models.CharField(
    max_length = 500
    )
    class Meta:
        verbose_name_plural = 'exercies'

    def __str__(self):
        "return"
        return self.category
