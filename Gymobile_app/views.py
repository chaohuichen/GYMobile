from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from.models import Workout,Day
from .forms import DayForm

def index(request):
    """Home page"""
    return render(request,'Gymobile_app/index.html')

def days(request):
    """show all the workouts"""
    days = Day.objects.order_by('date_added')
    context = {'days': days}
    return render(request,'Gymobile_app/days.html',context)

def day(request,day_id):
    """show a single workout and all its work"""
    day= Day.objects.get(id=day_id)
    exercises= day.workout_set.order_by('-date_added')
    context={'day':day,'exercises':exercises}
    return render(request,'Gymobile_app/day.html',context)

def new_day(request):
    """Add a new day."""
    if request.method != 'POST':
        #No data submitted; create a blank form.
        form=DayForm()
    else:
        #POST data submitted;process data.
        form = DayForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('Gymobile_app:days'))

    context = {'form':form}
    return render(request, 'Gymobile_app/new_day.html',context)

def profile(request):
    """Profile page"""
    return render(request,'Gymobile_app/index.html')

def account(request):
    """Account page"""
    return render(request,'Gymobile_app/index.html')
