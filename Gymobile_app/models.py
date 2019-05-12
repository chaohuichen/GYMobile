from django.db import models
from datetime import datetime,timedelta
# Create your models here.
class Day(models.Model):
    "A day the user is having"
    #day = models.DateTimeField(default=datetime.now()+timedelta(days=30))
    day = models.DateTimeField(default=datetime.now())

    def __str__(self):
        "..return"
        return str(self.day)

class workout(models.Model):
    "workout type"
    day = models.ForeignKey(Day,on_delete=models.CASCADE)
    exercise = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'workouts'

    def __str__(self):
        "return"
        return self.exercise[:50]+"..."
