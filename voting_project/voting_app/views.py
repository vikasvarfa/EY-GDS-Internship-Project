from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.http import HttpResponse,HttpResponseRedirect
from .forms import ContactForm


def home(request):
    return render(request, 'home.html')

# def contact(request):
#     return render(request, 'contact.html')



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form_instance = form.save(commit=False)
            form_instance.save()
            # Redirect to a success page or any other desired page after successful form submission
            messages.success(request, "Your message sent successfully.")
            return redirect('contact')  # Assuming you have a 'contact_success' URL
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

# def signup(request):
    # return render(request, 'signup.html')
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')

        # Check if user with given email or username already exists
        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            messages.error(request, "User with this username or email already exists.")
            return redirect('signup')

        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        messages.success(request, "Account created successfully. You are now logged in.")
        return redirect('login')

    return render(request, 'signup.html')

# def login(request):
    # return render(request, 'login.html')

 
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully.")
            # return redirect('pages/index')  # Redirect to questions page after successful login
            return render(request,'pages/index.html')

        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')

    return render(request, 'login.html')

def questions(request):
    if 'username' not in request.session.keys():
        return HttpResponseRedirect('login')
    else:
        return render(request, 'questions.html')
def index(request):
    if 'username' not in request.session.keys():
        return HttpResponseRedirect('login')
    else:
        return render(request,'pages/index.html')
    
 