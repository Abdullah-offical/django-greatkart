from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Account
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split("@")[0] # split email to create user name
            # Create user function is define in model 
            user = Account.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password              
            )
            user.phone_number = phone_number
            user.save()
            messages.success(request, 'Registration Successfuly.')
            return redirect('register')
    else:
        form = RegistrationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/register.html', context)



def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        # Authenticate user
        user = auth.authenticate(email=email, password=password)
        
        
        if user is not None:
            auth.login(request, user)  # Log in the user
            return redirect('home')  # Redirect to home page after successful login
        else:
            messages.error(request, 'Invalid login credentials.')  # Display error message
            return redirect('login')  # Redirect back to login page on failure
    
    return render(request, 'accounts/login.html')

@login_required(login_url = 'login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'You are logged out!')
    return redirect('login')
