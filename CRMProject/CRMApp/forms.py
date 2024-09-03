# Two forms are needed.
# Form 1 - For a  new User, Form 2 - to Login

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record
from django.forms.widgets import PasswordInput, TextInput

#Register/Create a User
class CreateUser(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username','password1','password2']
        
#Login a User
class LoginUser(AuthenticationForm):
    
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
    
#AddRecord
class AddRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['first_name','email','phone','country']
        
#Update A Record
class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['first_name','email','phone','country']
