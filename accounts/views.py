from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .passwordValidator import Password

def signUp(request):
    if(request.method=='POST'):
        passwordMatch=Password.passwordValidate(request.POST['pwd1'])
        if(passwordMatch==False):
            return render(request,'accounts/SignUp.html',{'errorPass':'Password Rule not Fulfilled.Must have one UpperCase,One LoweCase,One Number and min 8 characters'})
        elif(request.POST['pwd1']==request.POST['pwd2']):
            try:
                user= User.objects.get(username=request.POST['userName'])
                return render(request,'accounts/SignUp.html',{'errorUser':'User name already Taken. Please Choose a Diferrent One'})
            except User.DoesNotExist:
                user= User.objects.create_user(request.POST['userName'],email=request.POST['email'],password=request.POST['pwd1'])
                auth.login(request,user)
                return render(request,'accounts/Login.html',{'succesUser':'User Succesfully Created, Please Login'})
        else:
            return render(request,'accounts/SignUp.html',{'errorPass':'Password Does Not Match. Please try once More'})
#        return True
    else:
#        return False
        return render(request,'accounts/SignUp.html')

def logIn(request):
    if(request.method=='POST'):
        user=auth.authenticate(username=request.POST['userName'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,'accounts/LogIn.html',{'errorPass':'UserName or Password does not Match'})
    else:
        return render(request,'accounts/LogIn.html')

def logOut(request):
    if(request.method=="POST"):
        auth.logout(request)
        return render(request,'accounts/Logout.html')
