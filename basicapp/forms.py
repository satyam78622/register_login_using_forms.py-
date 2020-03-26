from django import forms
from django.contrib.auth.models import User
from basicapp.models import userprofile

class myform(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    confirmpassword=forms.CharField(widget=forms.PasswordInput)
    class Meta():
        model=User
        fields=['first_name','last_name','email','username','password','confirmpassword']


class extraform(forms.ModelForm):
    class Meta():
        model=userprofile
        exclude=['user']
    
     
     