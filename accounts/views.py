from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

def register(request):
    if request.method=='POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email Taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,email=email,password=password1)
                user.save()
                print("user created")
                return redirect('login')
        else:
            messages.info(request,"Passwords aren't matching")
            return render(request,'register.html')
    else:
        return render(request,'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password1=request.POST['password']
        user=auth.authenticate(username=username,password=password1)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid cedentials')
            return redirect('login')
    else:
        return render(request,'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')

def delete_account(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        auth.logout(request)  # Log out the user after deletion
        messages.info(request, "Your account has been deleted.")
        return redirect('index')
    return render(request, 'delete_account.html')
 
