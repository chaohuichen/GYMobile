from django import forms

from .models import WorkoutLog,Exercise

class WorkoutLogForm(forms.ModelForm):
    class Meta:
        model = WorkoutLog
        fields = ['day']
        labels = {'text':''}

class ExerciseForm(forms.ModelForm):
    class Meta:
        model =Exercise
        fields = ['bodypart']
        labels = {'text':''}
        #widgets = {'text': forms.Textarea(attrs={'cols': 80})}
