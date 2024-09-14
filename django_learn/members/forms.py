from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter email'}),)
    first_name = forms.CharField(max_length = 100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'first name'}),)
    last_name = forms.CharField(max_length = 100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'last name'}),)
   

    class Meta:
        model  =  User

        fields = ('username','first_name','last_name','email','password1','password2')

        # fields = "__all__" # Gets all the columns
        # fields  = ('name','address') # Get only name , address column
        labels = {
             'username':'',
              'first_name':'',
               'last_name':'',
                'email':'',
                 'password1':'',
                  'password2':'',

        }
        widgets = {
            'username':forms.TimeInput(attrs={'class':'form-control','placeholder':'Enter name'}),
             
        }
    def __init__(self, *args, **kwargs):
        super(RegisterUserForm,self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
