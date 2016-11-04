from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone
from .forms import BlogPostForm
from django.shortcuts import redirect



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

def new_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect(post_details, post.pk)
    else:
        form = BlogPostForm(request.POST, request.FILES)
    return render(request, 'blogpostform.html', {'form' : form})

def edit_post(request):
    post=get_object_or_404(Post, pk=id)
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES,instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect(post_details, post.pk)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blogpostform.html', {'form' : form})
