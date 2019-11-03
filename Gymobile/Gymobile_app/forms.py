from django import forms

from .models import WorkoutLog,Exercies

class WorkoutLogForm(forms.ModelForm):
    class Meta:
        model =WorkoutLog
        fields = ['day']
        labels = {'text':''}

class ExerciesForm(forms.ModelForm):
    class Meta:
        model = Exercies
        fields = ['bodypart']
        labels = {'text':''}
        #widgets = {'text': forms.Textarea(attrs={'cols': 80})}
