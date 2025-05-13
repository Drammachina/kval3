from django.shortcuts import render
from .forms import RegisterForm
from django.views.generic import CreateView
from .models import Cart
from django.contrib.auth.decorators import login_required

class RegisterView(CreateView):
    form_class = RegisterForm
    success_url = '/login/'
    template_name = 'users/register.html'

@login_required
def index(request):
    carts = Cart.objects.all()
    return render(request, 'dashboard.html', {'carts': carts})