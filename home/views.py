from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from blog.models import Post


# Create your views here.
def home(request):
    return render(request, 'home/home.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        msgtype = request.POST['msgtype']
        message = request.POST['message']
        contact = Contact(name=name, email=email, phone=phone,
                          msgtype=msgtype, message=message)
        contact.save()
        messages.success(request, 'Message sent!')
        print(name, email, phone, msgtype, message)
    return render(request, 'home/contact.html')


def about(request):
    return render(request, 'home/about.html')


def search(request):
    query = request.GET['query']
    if len(query) > 80 or len(query) < 1:
        allPosts = Post.objects.none()
    else:
        titlesearch = Post.objects.filter(title__icontains=query)
        contentsearch = Post.objects.filter(content__icontains=query)
        authorsearch = Post.objects.filter(author__icontains=query)
        allPosts = titlesearch.union(contentsearch, authorsearch)

    params = {'allPosts': allPosts, 'query': query}
    return render(request, 'home/search.html', params)


def handleSignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # checks for errorneous inputs
        if len(username) < 8:
            messages.error(request, 'Username must be 8 or more characters')
            return redirect('home')
        if not username.isalnum():
            messages.error(
                request, 'Username must be alphanumeric. Should not contain special characters i.e. @#$%^&*<>!')
            return redirect('home')
        if pass1 != pass2:
            messages.error(
                request, 'Password and Confirm Password should be same')
            return redirect('home')
        if not fname.isalpha():
            messages.error(
                request, 'Name should not be alphanumeric. Should not contain special characters i.e. @#$%^&*<>!')
            return redirect('home')
        if not lname.isalpha():
            messages.error(
                request, 'Name should not be alphanumeric. Should not contain special characters i.e. @#$%^&*<>!')
            return redirect('home')
        # Create user

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(
            request, "Your account has been sucessfully created")
        return redirect('home')

    else:
        return HttpResponse('404 - Not Found')


def handleLogin(request):
    if request.method == 'POST':
        # loginusername = request.POST['username']
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']

        user = authenticate(username=loginusername, password=loginpass)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Invalid Credentials, Please try again")
            return redirect('home')

    return HttpResponse('404 - Not Found')


def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully Logged out")
    return redirect('home')
