from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    class Meta: 
        model = CustomUser
        fields=['first_name', 'last_name', 'email', 'phone', 'username', 'password1', 'password2']