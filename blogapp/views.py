from django.shortcuts import render,redirect
from .models import Post,Contact
from .forms import PostForm
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth import authenticate,login,logout

# Views created here.

# This function gets posts from Post model and renders index.html file
def index(request):
    post=Post.objects.all()
    return render(request , 'index.html',{'posts':post})

# This function gets a single post and renders it in detail on details.html 
def detail(request,id):
    post=Post.objects.get(pk=id)
    return render(request,'detail.html',{'post':post}) 

# This function creates new post using model(Post) from "forms.py" and redirects it to index page after saving.
def create_post(request):
    if request.method == 'POST':
        form  = PostForm(request.POST , request.FILES)
        if form.is_valid():
            form.save() 
            return redirect('/') 
    else:
        form = PostForm()
        return render(request, 'blog_post.html',{'form':form}) 

# This function updates the selected post based on ID and redirects to index page
def update_post(request,id):
    post = Post.objects.get(pk=id)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'updatepost.html',{'form':form})   

# This function delets the post based on given ID 
def delete_post(request,id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect('/')

# This function is being used to give access to users
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

# This function logs out the user 
def log_out(request):
    logout(request)
    return redirect('/')   

# This function renders the about us page
def aboutus(request):
    return render(request,'aboutus.html') 

#This function renders the contact us page 
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


              
