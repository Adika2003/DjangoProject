from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['club','title','description','start_time','end_time','location','published']
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for fname in ('start_time','end_time'):
            if fname in self.fields:
                self.fields[fname].input_formats = ['%Y-%m-%dT%H:%M']
