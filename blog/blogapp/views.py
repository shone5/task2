from django.core.files.storage import FileSystemStorage
from django.forms import forms
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from blogapp.models import BlogPost, CustomerDetails, Comments


def home_page(request):
    data = BlogPost.objects.all()
    data2=Comments.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        com = request.POST.get('comments')
        date = request.POST.get('date')
        obj = Comments(comments=com,title=title,date=date)
        obj.save()
    # if request.method == 'POST':
    #     tit = request.POST.get('title')
    #     des = request.POST.get('description')
    #     date = request.POST.get('date')
    #     img = request.FILES['image']
    #     obj = BlogPost(title=tit, description=des, date=date,image=img)
    #     obj.save()
    context = {
        'data': data,
        'data2': data2

    }

    return render(request, 'home_page.html',context)


def reply_comment(request):

    if request.method == 'POST':
        com = request.POST.get('comments')
        # date = request.POST.get('date')
        obj = Comments(comments=com)
        obj.save()

    return redirect(home_page)

def create_post(request):
    if request.method == 'POST':
        tit = request.POST.get('title')
        des = request.POST.get('description')
        date = request.POST.get('date')
        img = request.FILES['image']
        obj = BlogPost(title=tit, description=des, date=date, image=img)
        obj.save()
        return redirect(home_page)


def register_page(request):
    return render(request, 'register.html')

def login_page(request):
    return render(request, 'login_page.html')

def register(request):
    if request.method == "POST":
        un = request.POST.get('username')
        em = request.POST.get('email')
        pw = request.POST.get('password')
        cp = request.POST.get('confirmpassword')
        if CustomerDetails.objects.filter(username=un).exists():
            messages.warning(request,"This Username Or Email already exists. Please choose a different one.")
        elif CustomerDetails.objects.filter(username=None).exists():
            messages.warning(request, "Please Enter a different one.")
        elif CustomerDetails.objects.filter(email=em).exists():
            messages.warning(request,"This Username Or Email already exists. Please choose a different one.")
        elif pw == cp:
            obj = CustomerDetails(username=un, email=em, password=pw, confirmpassword=cp)
            obj.save()
            messages.success(request,"User Register Successfully")
            return redirect(login_page)
            # return render(request, 'login_page.html')
        else:
            messages.warning(request,"Sorry.... Invalid Username Or Password")
            return redirect(register_page)
            # return render(request, 'register.html')
    return render(request, 'register.html', {'msg': "sorry.... password not matched"})


def login(request):
    if request.method == 'POST':
        username_r = request.POST.get("username")
        password_r = request.POST.get("password")
        if CustomerDetails.objects.filter(username=None).exists():
            messages.warning(request, "Please Enter a different one.")
        elif CustomerDetails.objects.filter(username=username_r, password=password_r).exists():
            request.session['username'] = username_r
            request.session['password'] = password_r
            messages.success(request,"User Login successfully")

            return redirect(home_page)
        else:
            messages.warning(request,"Sorry.... Invalid Username Or Password")
            return redirect(login_page)

    return render(request, 'login_page.html', {'msg': "sorry.... invalid username or password"})


def logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(login)