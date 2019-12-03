from django.contrib.auth.models import User
from django.db import models, IntegrityError
from django.shortcuts import reverse
from django.utils import timezone

TASK_CHOICES = (
    ('to do','TODO'),
    ('doing','DOING'),
    ('done','DONE'),
)

class Feature(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    votes = models.ManyToManyField(User, related_name='feature_votes', blank=True)
    comments_count = models.IntegerField(default=0)
    status = models.CharField(max_length=6, choices=TASK_CHOICES, default='to do')
    price = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
        
    def total_votes(self):
        return self.votes.count()
    
    def get_absolute_url(self):
        return reverse("featureview", kwargs={"id": self.id})
        
class Comment(models.Model):
    feature = models.ForeignKey(Feature, related_name='user_comment', null=True, on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='comment_author', blank=True, on_delete=models.CASCADE)
    text = models.TextField()
    i_want_this_too = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    
    def __unicode__(self):
        return self.feature
        
    def __str__(self):
        return self.feature
