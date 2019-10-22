from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

TASK_CHOICES = (
    ('to do','TODO'),
    ('doing','DOING'),
    ('done','DONE'),
)

class Bug(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    # votes = models.ManyToManyField(User, blank=True, related_name="votes")
    # number_of_likes = models.IntegerField(default=0)
    # comments_count = models.IntegerField(default=0)
    status = models.CharField(max_length=6, choices=TASK_CHOICES, default='to do')
    
    def __str__(self):
        return self.title
"""    
class Comment(models.Model):
    bug = models.ForeignKey(Bug, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, blank=True)
    text = models.TextField()
    i_have_this_too = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    update_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    
    def __str__(self):
        return self.user.username

class reply_for_comment(models.Model):
    user = models.ManyToManyField(User, null=True, blank=False)
    comment = models.ForeignKey(Comment, null=True, on_delete=models.CASCADE)
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    update_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
"""  
    