from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect,Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Exercise,WorkoutLog
from .forms import ExerciseForm,WorkoutLogForm

def index(request):
    """Home page"""
    return render(request,'Gymobile_app/index.html')

@login_required
def workoutlogs(request):
    """show all the workouts"""
    workoutlogs = WorkoutLog.objects.filter(owner=request.user).order_by('date_added')
    context = {'workoutlogs': workoutlogs}
    return render(request,'Gymobile_app/workoutlogs.html',context)

@login_required
def workoutlog(request,workoutlog_id):
    """show a single workout and all its work"""
    workoutlog= get_object_or_404(WorkoutLog,id=workoutlog_id)

    # Make sure the day belongs to current user.
    if workoutlog.owner !=request.user:
        raise Http404

    exercises= workoutlog.exercise_set.order_by('-date_added')
    context={'workoutlog':workoutlog,'exercises':exercises}
    return render(request,'Gymobile_app/workoutlog.html',context)

@login_required
def new_log(request):
    """Add a new log."""
    if request.method != 'POST':
        #No data submitted; create a blank form.
        form=WorkoutLogForm()
    else:
        #POST data submitted;process data.
        form = WorkoutLogForm(request.POST)
        if form.is_valid():
            new_log=form.save(commit=False)
            new_log.owner=request.user
            new_log.save()
            return HttpResponseRedirect(reverse('Gymobile_app:workoutlogs'))

    context = {'form':form}
    return render(request, 'Gymobile_app/new_log.html',context)

@login_required
def new_exercise(request,workoutlog_id):
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
