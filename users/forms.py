from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User # django built-in User models
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1','password2')

# Stock Info  Forms
class StockInfoForm(ModelForm):
    class Meta:
        model = StockInfo
        fields = '__all__' # or list of fields if needed

class StockInfoToUpdateForm(forms.ModelForm):
    class Meta:
        model = StockInfo
        fields = ['codeAction', 'pays', 'industrie', 'resultat', 'potentiel', 'montantDividende', 'commentaires']
