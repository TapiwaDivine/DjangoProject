from django.db import models
from django.contrib.auth.models import User

USER_GENDER = (
    ('undefined','UNDEFINED'),
    ('woman','Woman'),
    ('man','MAN'),
)

class Profile(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    age = models.IntegerField(default='')
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    location = models.CharField(max_length=140, default=None)  
    gender = models.CharField(max_length=6, choices=USER_GENDER, default='undefined')  
    bio = models.CharField(max_length=240, null=True)
    
    def __str__(self):
        return f'{self.user.username} Profile'