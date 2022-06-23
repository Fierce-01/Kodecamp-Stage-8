from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def Signup(request):
    if request.method == 'POST':
        user_data = UserCreationForm(request.POST)
        if user_data.is_valid:
            user_data.save()
            return redirect("accounts:signinview")
        else:
            return redirect("accounts:signnupview")
    context = {
        'form': UserCreationForm
    }
    return render(request, 'accounts/signup.html', context)
