from django import forms

from .models import Day,Workout

class DayForm(forms.ModelForm):
    class Meta:
        model =Day
        fields = ['day']
        labels = {'text':''}

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['exercise']
        labels = {'text':''}
        #widgets = {'text': forms.Textarea(attrs={'cols': 80})}
