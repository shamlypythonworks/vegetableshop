from django.contrib import messages
from django.contrib.auth.models import  User,auth
# Create your views here.
from django.shortcuts import redirect,render
def appointment(request):
   return render(request,"register.html")

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        name = request.POST['name']
        email = request.POST['e_mail']
        password1 = request.POST['pswd']
        password2 = request.POST['repswd']
        chkbox = request.POST['chkbox']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "sorry username already exists")
                return redirect('registerdet')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"sorry email already exist")
                return redirect('registerdet')
            else:
                user = User.objects.create_user(username=username,first_name=name,email=email,password=password1,
                                         )
                user.save()
                messages.info(request,'you r successfully registered ')
                return redirect('/')
        else:
            messages.info(request, "password mismatch")
            return redirect('registerdet')
def login(request):
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['psw']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            messages.info(request, "you r logged in")
            return redirect('/')
        else:
            messages.info(request,"it is not valid")
            return redirect('login')
    else:
        return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')























