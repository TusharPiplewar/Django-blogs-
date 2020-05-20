
from django import forms
from .models importuploadForm

from django.contrib.auth.models import User
class uploadForm(forms.ModelForm):
    class Meta:
        model=Upload
        fields=('name','description','pic') # include all field in form
        #fields=('eid','ename','salary')  #includes perticular fields
        #exclude=['salary'] #exclude perticular field
        #widgets={'address':forms.Textarea(attrs={'rows':3,'cols':30})}

class SignUpForm(forms.ModelForm):
    class Meta:
        model=User
        #fields='__all__'
        fields=('username','password','email','first_name','last_name')
        widgets={'password':forms.PasswordInput()}


#
