from django import forms
from post.models import PostEvent
from datetime import date, time

class postEventForm(forms.ModelForm):

    class Meta:
        model = PostEvent
        fields = ['title','Place','Date','Time','body','image']
        widgets = {
                'Date':forms.DateInput(attrs={'class':'form','type':'date'}),
                'Time': forms.TimeInput(attrs={'class':'form','type':'time'}),
        }
