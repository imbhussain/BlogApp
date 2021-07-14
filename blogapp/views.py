from django.shortcuts import render,redirect
from .models import Post,Contact
from .forms import PostForm
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def index(request):
    post=Post.objects.all()
    return render(request , 'index.html',{'posts':post})


def detail(request,id):
    post=Post.objects.get(pk=id)
    return render(request,'detail.html',{'post':post}) 

def create_post(request):
    if request.method == 'POST':
        form  = PostForm(request.POST , request.FILES)
        if form.is_valid():
            form.save() 
            return redirect('/') 
    else:
        form = PostForm()
        return render(request, 'blog_post.html',{'form':form}) 


def update_post(request,id):
    post = Post.objects.get(pk=id)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'updatepost.html',{'form':form})   

def delete_post(request,id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect('/')


def log_in(request):
    if  request.method =='POST':
        fm=AuthenticationForm(request.POST, data=request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            user=authenticate(username=uname, password=upass)
            if user is not None:
                login(request , user)
                return redirect('/')        
    else:
        fm=AuthenticationForm()
    return render(request,'login.html',{'form':fm})  


def log_out(request):
    logout(request)
    return redirect('/')   


def aboutus(request):
    return render(request,'aboutus.html') 


def contactus(request):
    if  request.method =='POST':
            fname=request.POST.get('fullname')
            email=request.POST.get('email')
            msg=request.POST.get('message')
            print(msg)
            contact=Contact(fullname=fname, email=email,message=msg)
            print(contact)
            contact.save()
            return redirect('/')
    return render(request,'contactus.html')


              
