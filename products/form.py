from django import forms
from .models import Product, ProductDetail, OrderDetail
# class Productform(forms.ModelForm):
#   class Meta:
#     model = ProductDetail
#     fields = ['nameProduct','decripsion','image','cost','amount','status']

class LoginForm(forms.Form):
  username = forms.CharField(max_length=50)
  password = forms.CharField(max_length=50, widget=forms.PasswordInput)

class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderDetail
        fields = ['cost', 'quanity', 'product', 'order']