from django.shortcuts import render,HttpResponse
from home.models import Contact
from blog.models import Post
from django.contrib import messages


# Create your views here.
def home(request):
    allPosts = Post.objects.all()
    content = {'posts': allPosts}
    return render(request, 'home/index.html', content)

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    # messages.success(request, 'Welcome to our Contact Page')
    if request.method=='POST':
        fullname = request.POST['fullname']
        email = request.POST['email']
        msg = request.POST['msg']
        if len(fullname)<4 or len(email)<5 or len(msg)<10:
            messages.error(request, 'Please fill out the data correctly.')
        else:
            contact_info = Contact(fullname=fullname, email=email, msg=msg)
            contact_info.save()
            messages.success(request, 'Thanks '+fullname+' for contacting ThePunchCoders. We will get back to you soon.')
        
    
    return render(request, 'home/contact.html')

def search(request):
    s_query = request.GET['q']
    if len(s_query)>80:
        posts = []
    else:
        s_title = Post.objects.filter(post_title__icontains=s_query)
        s_desc = Post.objects.filter(post_desc__icontains=s_query)
        s_author = Post.objects.filter(post_author__icontains=s_query)
        s_title = s_title.union(s_author)
        posts = s_title.union(s_desc)
    content = {'posts': posts,'query': s_query}
    return render(request, 'home/search.html', content)