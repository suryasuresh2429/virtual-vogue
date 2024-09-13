from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.core.files.base import ContentFile
import base64
from io import BytesIO
def home(request):
    return render(request,'index.html')
@login_required
def tryon(request):
  return render(request,'tryon.html')
# @login_required
def user_profile(request):
  return render(request,'user_profile.html')
def about(request):
  return render(request,'about.html')
#E-cart
def buy_now(request):
    return render(request, 'buy_now.html')
def buy_now1(request):
    return render(request, 'buy_now1.html')
def buy_now2(request):
    return render(request, 'buy_now2.html')
def buy_now3(request):
    return render(request, 'buy_now3.html')
def buy_now4(request):
    return render(request, 'buy_now4.html')
def buy_now5(request):
    return render(request, 'buy_now5.html')
def buy_now6(request):
    return render(request, 'buy_now6.html')
def buy_now7(request):
    return render(request, 'buy_now7.html')
def buy_now8(request):
    return render(request, 'buy_now8.html')
def add_to_cart(request):
    return render(request, 'add_to_cart.html')
def checkout(request):
    return render(request, 'checkout.html')
def wishlist(request):
    return render(request, 'wishlist.html')