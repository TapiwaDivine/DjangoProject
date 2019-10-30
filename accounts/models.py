from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

USER_GENDER = (
    ('undefined','UNDEFINED'),
    ('female','FEMALE'),
    ('male','MALE'),
)

class Profile(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    age = models.IntegerField(default='')
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    location = models.CharField(max_length=140, default='')  
    gender = models.CharField(max_length=6, choices=USER_GENDER, default='undefined')  
    bio = models.CharField(max_length=240, default='')
    
    def __str__(self):
        return f'{self.user.username} Profile'

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = Profile.objects.create(user=kwargs['instance'])
post_save.connect(create_profile, sender=User)   
    
    