from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from home.models import Contact,TeamMember
from blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.


# Home Functiuon starrt

def index(request):
    posts = Post.objects.order_by('-Stmp')[:3]
    params = {'posts':posts}
    return render(request,'home/index.html',params)


# About Functiuon start

def about(request):
    allMember = TeamMember.objects.all()
    params = {'members':allMember}
    return render(request,'home/about.html',params)


# def MemberDetails(request,slug):
#     members = TeamMember.objects.filter(member_slug=slug).first()
#     params = {'member':members}
#     return render(request,'home/memberDetails.html', params)

# contact function start

def contact(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']

        if len(name)<3 or len(phone)<10 or len(content)<6:
             messages.error(request,'Please Fill The From Corectly')
        else:
            contact = Contact(name=name,email=email,phone=phone,content=content)
            contact.save()
            messages.success(request,'Your Message SuccusFully Send')

        print(name,email,phone,content)
    return render(request,'home/contact.html')

# contact function end

# singup function start

def getSingup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if len(username) > 10:   
            messages.error(request,"Please Use Under 10 Charchter ")
            return redirect('/')

        if not username.isalnum():   
            messages.error(request,"Please use Number and Cherchter  mixed 10")
            return redirect('/')

        if pass1 != pass2:   
            messages.error(request,"Don,t Match Your Password")
            return redirect('/')


        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,"Your Conding Point Account Succussfully Created")

        return redirect('/')

    else:
        return HttpResponse('404 - Not Found')

# singup function end

# login Functiuon start

def getLogin(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['pass']

        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            messages.success( request,"You Successfully Logged In")
            return redirect('/')
        else:
            messages.error(request,'Invalid Account ! Please Create a Account And  Login')
            return redirect('/')

    return HttpResponse('404 - Not Found')

# login Functiuon end

# logOut Functiuon start

def getLogOut(request):
    logout(request)
    messages.success( request,"You Successfully Logged out")
    return redirect('/')

# logOut Functiuon End


# search function start

def search(request):
    query = request.GET['query']
    if len(query) > 80:
        allPosts = Post.objects.none()
    elif len(query) == 0:
        allPosts = Post.objects.none()

    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query) 
        allPosts =allPostsTitle.union(allPostsContent)
    params = {"posts":allPosts,'query':query}
    return render(request,'home/search.html',params)

# search function end
