from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth import get_user_model
from .models import Product


def index(request):
    return render(request, 'index.html')

def blog(request):
    return render(request, 'blog.html')

def services(request):
    return render(request, 'services.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def shop(request):
    pro = Product.objects.all()
    return render(request, 'shop.html',{'pros':pro})

def thankyou(request):
    return render(request, 'thankyou.html')


# ---------------------------
#   LOGIN FUNCTION (FIXED)
# ---------------------------
def login(request):
    if request.method == 'POST':
        un = request.POST.get('uname')
        p1 = request.POST.get('pass1')

        user = auth.authenticate(username=un, password=p1)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('/')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('/login/')

    return render(request, 'login.html')


# ---------------------------
#   LOGOUT
# ---------------------------
def logout(request):
    auth.logout(request)
    print('Logout successfully!')
    return redirect('/login/')


# ---------------------------
#   REGISTER PAGE
# ---------------------------
def register(request):
    # Handle registration form POST
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        un = request.POST.get('uname')
        p1 = request.POST.get('pass1')
        p2 = request.POST.get('pass2')

        # Basic validation
        if not (un and p1 and p2 and email):
            messages.error(request, 'Please fill in all required fields.')
            return redirect('/register/')

        if p1 != p2:
            messages.error(request, 'Passwords do not match.')
            return redirect('/register/')

        User = get_user_model()
        if User.objects.filter(username=un).exists():
            messages.error(request, 'Username already taken — please choose another.')
            return redirect('/register/')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'An account with that email already exists.')
            return redirect('/register/')

        # Create user
        user = User.objects.create_user(username=un, password=p1, email=email, first_name=fname or '', last_name=lname or '')
        user.save()
        messages.success(request, 'Registration successful. You can now log in.')
        return redirect('/login/')

    return render(request, 'register.html')

def forgotpassword(request):
    return render(request, 'forgotpassword.html')
