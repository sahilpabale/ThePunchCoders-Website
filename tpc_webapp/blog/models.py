from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    post_title = models.CharField(max_length=200)
    post_desc = models.TextField()
    post_author = models.CharField(max_length=100)
    post_pub_date = models.DateTimeField()
    # post_comment
    # post_thumb = models.ImageField(upload_to="images/blog/thumbnails")
    post_slug = models.CharField(max_length=300)

    def __str__(self):
        return self.post_title + ' by ' + self.post_author
    

'''
Comment Model Elements:
> comment_id
> comment_desc
> user(assc.)
> post(assc.)
> parent_comment(new comment = Null, Reply = Parent Asscociation)
> timestamp
'''

# Comment Model
class BlogComment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    comment_desc = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent_comm = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment_desc[0:20] + '.. by '+self.user.username
    