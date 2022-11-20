from django.shortcuts import render
from blog.models import Post, Comment
from . forms import CommentForm

# Create your views here.
def blog_index(request):
    post = Post.objects.all().order_by("-created_on")
    context = {
        "posts": post,
    }
    return render(request, "blog_index.html", context)
    
def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains = category
    ).order_by("-created_on")
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog_category.html", context)

def blog_detail(request, id):
    post = Post.objects.get(id=id)

    form = CommentForm()
    if request.method == 'POST':
        print(f"\n\n\Comment\n\n")
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()
            comment = ""
    comments = Comment.objects.filter(post=post).order_by("-created_on")
    print(f"\n\n\Comments:{comments}n\n\n")
    context = {
        "post":post,
        "comments": comments,
        "form":form
    }
    return render(request, "blog_detail.html", context)
