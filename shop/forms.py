from django.forms import ModelForm
from shop.models import Brands,Mobile,Order,Cart
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BrandCreateForm(ModelForm):
    class Meta:
        model=Brands
        fields='__all__'

class MobileCreationForm(ModelForm):
    class Meta:
        model =Mobile
        fields = '__all__'

class UserRegForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password1','password2']

class OrderForm(ModelForm):
    class Meta:
        model=Order
        fields='__all__'

class CartForm(ModelForm):
    class Meta:
        model=Cart
        fields='__all__'

