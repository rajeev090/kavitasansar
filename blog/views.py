from django.shortcuts import render, HttpResponse
from blog.models import Post


# Create your views here.

def blogHome(request):

    allPosts = Post.objects.order_by('-sno')
    context = {'allPosts': allPosts}
    return render(request, 'blog/bloghome.html', context)


def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    return render(request, 'blog/blogpost.html', {'post': post})
