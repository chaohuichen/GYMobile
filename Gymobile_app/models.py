from django.db import models
from datetime import datetime,timedelta
# Create your models here.
class Day(models.Model):
    "A day the user is having"
    #day = models.DateTimeField(default=datetime.now()+timedelta(days=30))
    def number():
        no = Day.objects.count()
        if no == None:
            return 1
        else:
            return no + 1

    day = models.IntegerField(('Workout day'), unique=True,default=number)
    date_added = models.DateTimeField(auto_now_add=True)
    #owner = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        "..return"
        return 'Workout Day '+str(self.day)

class Workout(models.Model):
    "workout type"
    Back='Back Day'
    Leg='Legs Day'
    Shoulder='Shoulder Day'
    Chest='Chest Day'
    type_of_workout=[
    (Back,'Back'),
    (Leg,'Leg'),
    (Shoulder,'Shoulder'),
    (Chest,'Chest'),
    ]

    day = models.ForeignKey(Day,on_delete=models.CASCADE)
    exercise = models.CharField(
        max_length=15,
        choices=type_of_workout,
        default=Back,)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'workouts'

    def __str__(self):
        "return"
        return self.exercise
