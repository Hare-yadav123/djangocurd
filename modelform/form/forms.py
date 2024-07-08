from django import forms
from. models import StudentModel
from django.core import validators
class ModelForm(forms.ModelForm):
    name=forms.CharField(max_length=100 )
    class Meta:
        model=StudentModel
        fields=['id','name','roll','city']

        labels={'name':'Enter your name','roll':'Enter your roll','city':'Enter your city'}
        help_text={'name':'Enter your Full name','roll':'Enter your roll Number','city':'Enter your city Name'}

        error_messages = {'name':{'required':'name field is required'},
                    'roll':{'required':'roll number is ness'},
                    'city':{'required':'city name is neeeded'}
                    }
        
        widgets={'name':forms.TextInput(attrs={'class':'myclass','placeholder':'write your name'}),
                'roll':forms.NumberInput(attrs={'class':'myclass','placeholder':'Eneter roll number'}),
                'city':forms.TextInput(attrs={'class':'myclass','placeholder':'write your city name'})}