from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect,Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Exercies,WorkoutLog
from .forms import ExerciesForm,WorkoutLogForm

def index(request):
    """Home page"""
    return render(request,'Gymobile_app/index.html')

@login_required
def days(request):
    """show all the workouts"""
    days = WorkoutLog.objects.filter(owner=request.user).order_by('date_added')
    context = {'days': days}
    return render(request,'Gymobile_app/days.html',context)

@login_required
def day(request,day_id):
    """show a single workout and all its work"""
    day= get_object_or_404(WorkoutLog,id=day_id)
    # Make sure the day belongs to current user.
    if day.owner !=request.user:
        raise Http404

    exercises= day.workout_set.order_by('-date_added')
    context={'day':day,'exercises':exercises}
    return render(request,'Gymobile_app/day.html',context)

@login_required
def new_day(request):
    """Add a new day."""
    if request.method != 'POST':
        #No data submitted; create a blank form.
        form=WorkoutLogForm()
    else:
        #POST data submitted;process data.
        form = WorkoutLogForm(request.POST)
        if form.is_valid():
            new_day=form.save(commit=False)
            new_day.owner=request.user
            new_day.save()
            return HttpResponseRedirect(reverse('Gymobile_app:days'))

    context = {'form':form}
    return render(request, 'Gymobile_app/new_day.html',context)

@login_required
def new_exercise(request,day_id):
    """add an exercise for a particular day"""
    day = WorkoutLog.objects.get(id=day_id)
    if request.method != 'POST':
        #No data submitted; create a blank form.
        form=ExerciesForm()
    else:
        #POST data submitted;process data.
        form = ExerciesForm(data=request.POST)
        if form.is_valid():
            new_exercise=form.save(commit=False)
            new_exercise.day=day
            new_exercise.save()
            return HttpResponseRedirect(reverse('Gymobile_app:day',
                                                args=[day_id]))
    context={'day':day,'form':form}
    return render(request,'Gymobile_app/new_exercise.html',context)

@login_required
def edit_exercise(request,workout_id):
    """Edit an exisiting entry"""
    workout = Exercies.objects.get(id=workout_id)
    day = workout.day
    if day.owner !=request.user:
        raise Http404

    if request.method != 'POST':
        #No data submitted; create a blank form.
        form=ExerciesForm(instance=workout)
    else:
        #POST data submitted;process data.
        form = ExerciesForm(instance=workout,data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('Gymobile_app:day',
                                                args=[day.id]))
    context={'workout':workout,'day': day,'form':form }
    return render(request,'Gymobile_app/edit_exercise.html',context)

@login_required
def delete_exercise(request,day_id):
    workout = Exercies.objects.get(id=workout_id)
    day = workout.day
    if day.owner !=request.user:
        raise Http404

    workout.delete()
    return render(request,'Gymobile_app/edit_exercise.html',context)
#creating a map view
@login_required
def map(request):
    return render(request, 'Gymobile_app/map.html')
