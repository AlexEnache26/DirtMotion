from django import forms
from .models import Item, ItemImage
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.models import inlineformset_factory


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

class ItemImageForm(forms.ModelForm):
    class Meta:
        model = ItemImage
        fields = ['image', 'is_main']

ItemImageFormSet = forms.inlineformset_factory(Item, ItemImage, form=ItemImageForm, extra=3, can_delete= True)