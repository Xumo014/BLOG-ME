from django.shortcuts import render
from .models import Post
from .forms import CommentForm
from skills.models import Skills, Abouts
# Create your views here.

def getPosts(request):
    posts = Post.objects.all()
    return render(request, "postapp/list.html", context={"posts": posts})

def getPost(request, pk):
    post = Post.objects.get(pk=pk)
    comments = post.comments.all()
    comment_form = CommentForm()
    tags = post.tags.all()
    
    if request.method=='POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            cf = comment_form.save(commit=False)
            cf.post_id = post.id
            cf.save()
    return render(request, "postapp/detail.html", context={"post":post, "comment_form": comment_form, "comments":comments, "tags": tags})


def getPostbytag(request, tagname):
    filter = True
    posts = Post.objects.filter(tags_name = tagname)
    template_name = 'postapp/list.html'
    context = {"posts": posts}
    return render(request, template_name=template_name, context=context) 

def About(request):
    skills = Skills.objects.all()
    abouts = Abouts.objects.all()
    template_name = "about.html"
    context = {"skills": skills, "abouts": abouts}
    return render(request, template_name=template_name, context=context)