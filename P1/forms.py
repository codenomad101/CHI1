from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Org


class CreateUserForm (UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']



class OrgForm(ModelForm):
    class Meta:
        model = Org
        fields = ['name','Otype','Csize','Place']


# class CutomerForm(ModelForm):
#     class Meta:
#         model = Customer
#         fields = '__all__'