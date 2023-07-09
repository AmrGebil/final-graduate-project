from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile
class RegisterForm(UserCreationForm):
    # fields we want to include and customize in our form
    first_name = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name',
                                                               'class': 'form-control',
                                                               }))
    last_name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name',
                                                              'class': 'form-control',
                                                              }))
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                           'class': 'form-control',
                                                           }))
    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']




class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    password = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                 'class': 'form-control',
                                                                 'data-toggle': 'password',
                                                                 'id': 'password',
                                                                 'name': 'password',
                                                                 }))
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']

class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    # bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    first_name = forms.CharField(max_length=30, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=30, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    age = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(max_length=15, required=False,widget=forms.TextInput(attrs={'class': 'form-control'}))
    illnesses_numbers = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    illnesses = forms.CharField(max_length=30, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    illnesses_descriptions = forms.CharField(max_length=600, required=False,
                                             widget=forms.Textarea(attrs={'class': 'form-control'}))
    allergies = forms.CharField(max_length=150, required=False, widget=forms.Textarea(attrs={'class': 'form-control'}))
    surgeries = forms.CharField(max_length=150, required=False, widget=forms.Textarea(attrs={'class': 'form-control'}))
    immunizations = forms.CharField(max_length=150, required=False,
                                    widget=forms.Textarea(attrs={'class': 'form-control'}))
    results_of_physical_exams_and_tests = forms.CharField(max_length=150, required=False,
                                                          widget=forms.Textarea(attrs={'class': 'form-control'}))
    physical_exams_and_tests_images = forms.ImageField(required=False)
    medicines = forms.CharField(max_length=150, required=False, widget=forms.Textarea(attrs={'class': 'form-control'}))
    medicines_images = forms.ImageField(required=False)
    medical_rays = forms.CharField(max_length=150, required=False,
                                   widget=forms.Textarea(attrs={'class': 'form-control'}))
    medical_rays_images = forms.ImageField(required=False)
    health_habits = forms.CharField(max_length=150, required=False,
                                    widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Profile
        fields = ['avatar','first_name','last_name','age','phone_number', 'illnesses_numbers', 'illnesses', 'illnesses_descriptions', 'allergies',
                'surgeries', 'immunizations', 'results_of_physical_exams_and_tests', 'physical_exams_and_tests_images', 'medicines', 'medicines_images', 'medical_rays', 'medical_rays_images','medical_rays', 'health_habits',]











