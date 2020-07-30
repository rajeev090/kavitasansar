from django.shortcuts import render, HttpResponse
from home.models import Contact
from django.contrib import messages
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
