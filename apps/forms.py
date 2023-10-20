from django import forms
from .models import Users1
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField,UserChangeForm
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.models import Group


class StudentRegistration(forms.ModelForm):
    class Meta:
        model=Users1
        fields=['name','email','password']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'})
        }

# class RegistrationForm(UserCreationForm):
#     password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput)
#     group = forms.ModelChoiceField(
#         queryset=Group.objects.all(),
#         widget=forms.Select,
#         required=True,
#         label="User Group"
#     )

#     class Meta:
#         model = User
#         fields=['username','first_name','last_name','email']
#         labels={'email':'Email'}


class RegistrationForm(UserCreationForm):
    password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'email':'Email'}



class loginform(AuthenticationForm):
   username = UsernameField(widget = forms.TextInput(attrs = {'autofocus':True,'class':'form-control'}))
   password = forms.CharField(label = _("Password"), strip = False, widget = forms.PasswordInput(attrs = {'autocomplete':'current-password','class':'form-control'}))



class EditUserProfileForm(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','date_joined','last_login']    
        labels={'email':'Email','first_name':'First Name','last_name':'Last Name'}


class EditAdminUserProfileForm(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']  
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            
        }  
        # labels={'email':'Email','first_name':'First Name','last_name':'Last Name'}
