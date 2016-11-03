from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone


# Create your views here.

def post_list(request):
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blogpost.html', {'posts': posts})



"""

create a view that returns a single Post object based on the post ID and render
it to the "postdetail.html" template or return a 404 error if the post is not found
"""
def post_details(request,id):
    post = get_object_or_404(Post, pk=id)
    post.views +=1 #clock up no of views
    post.save()
    return render(request, "postdetail.html", {'post':post})