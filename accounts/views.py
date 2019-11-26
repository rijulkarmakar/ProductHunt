from django.shortcuts import render,get_object_or_404

def signUp(request):
    return render(request,'accounts/SignUp.html')

def logIn(request):
    return render(request,'accounts/LogIn.html')

def logOut(request):
    return render(request,'accounts/SignUp.html')
