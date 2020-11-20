from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return redirect('profile-edit') 
    else:
        return redirect('login') 