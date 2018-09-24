from django import forms
from app_Two.models import User


# class FormUser(forms.Form):
#     first_name = forms.CharField()
#     last_name = forms.CharField()
#     email = forms.EmailField()

class NewUserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = '__all__'
