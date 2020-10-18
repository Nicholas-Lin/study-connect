from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request, 'social_app/index.html')
    else:
        return redirect('/login') 