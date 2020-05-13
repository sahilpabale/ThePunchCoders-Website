from django.shortcuts import render, HttpResponse, redirect
from .models import Post, BlogComment
from django.contrib import messages
from blog.templatetags import extras

# Create your views here.
def blogHome(request):
    allPosts = Post.objects.all()
    content = {'allPosts': allPosts}
    return render(request, 'blog/blogHome.html', content)


def blogPost(request, slug):
    post = Post.objects.filter(post_slug=slug).first() # first() is used to get the query not the query set.
    comments = BlogComment.objects.filter(blog_post=post, parent_comm=None)
    replies = BlogComment.objects.filter(blog_post=post).exclude(parent_comm=None)
    replyDict = {}
    for reply in replies:
        if reply.parent_comm.comment_id not in replyDict.keys():
            replyDict[reply.parent_comm.comment_id] = [reply]
        else:
            replyDict[reply.parent_comm.comment_id].append(reply)

    # print(replyDict)
    params = {'post':post, 'comments':comments, 'user':request.user, 'replyDict':replyDict}
    return render(request, 'blog/blogPost.html',params)


def postComment(request):
    if request.method=='POST':
        comment = request.POST.get('comment',False)
        user = request.user
        post_id = request.POST.get('post_id')
        post = Post.objects.get(post_id=post_id)
        parent_id = request.POST.get('parent_id')
        if not comment:
            messages.error(request, 'Please enter something')
            return redirect(f"/blog/{post.post_slug}")

        if parent_id == "":
            comment_obj = BlogComment(comment_desc=comment, user=user, blog_post=post)
            comment_obj.save()
            messages.success(request, 'Your comment has been posted successfully')
        else:
            parent = BlogComment.objects.get(comment_id=parent_id)
            comment_obj = BlogComment(comment_desc=comment, user=user, blog_post=post, parent_comm=parent)
            comment_obj.save()
            messages.success(request, 'Your reply has been posted successfully')

        
        return redirect(f"/blog/{post.post_slug}")
    else:
        return redirect('/')
