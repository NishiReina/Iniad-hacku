from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views import generic

# Create your views here.
def home(request):
    return render(request, 'authtest/home.html')

@login_required
def private_page(request):
    return render(request, 'authtest/private.html', {})

def public_page(request):
    return render(request, 'authtest/public.html', {})

class SignUpView(generic.CreateView):
  form_class = UserCreationForm
  success_url = reverse_lazy('login')
  template_name = 'authtest/signup.html'