from django import forms
from django.forms import widgets
from .models import Notes, HomeWork, Todo
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class NotesForm(forms.ModelForm):
    class Meta:
        model=Notes
        fields=['title', 'description']

class DateInput(forms.DateInput):
    input_type='date'

class HomeworkForm(forms.ModelForm):
    class Meta:
        model = HomeWork
        widgets = {'due':DateInput()}
        fields = ["id","subject","title","description","due","is_finished"]
        

# that is comman class for wiki,todo, youtube
class DashboardForm(forms.Form):
    text=forms.CharField(max_length=100, label="Enter Your Search ")
    
    
# todo
class TodoForm(forms.ModelForm):
    class Meta:
        model=Todo
        fields=['title', 'is_finished']
        
#conversion
class ConversionForm(forms.Form):
    CHOICES=[('length','Length'),('mass','Mass')]
    measurement= forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    
class ConversionLengthForm(forms.Form):
    CHOICES=[('yard','Yard'),('foot','Foot')]
    input=forms.ChoiceField(required=False,widget=forms.TextInput(attrs={'type':'number','placeholder':'Enter The Number'}))
    measure1=forms.CharField(label="", widget= forms.Select(choices=CHOICES))
    measure2=forms.CharField(label="", widget= forms.Select(choices=CHOICES))


class ConversionMassForm(forms.Form):
    CHOICES=[('pound','Pound'),('kilogram','Kilogram')]
    input=forms.ChoiceField(required=False,widget=forms.TextInput(attrs={'type':'number','placeholder':'Enter The Number'}))
    measure1=forms.CharField(label="", widget= forms.Select(choices=CHOICES))
    measure2=forms.CharField(label="", widget= forms.Select(choices=CHOICES))
    

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model= User
        fields=['username','password1', 'password2']
            
