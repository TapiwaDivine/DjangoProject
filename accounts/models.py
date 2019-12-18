from django.db import models
from django.contrib.auth.models import User
from PIL import Image

USER_GENDER = (
    ('undefined','UNDEFINED'),
    ('female','FEMALE'),
    ('male','MALE'),
)

class Profile(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    age = models.IntegerField(default=0)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    location = models.CharField(max_length=140, default='')  
    gender = models.CharField(max_length=12, choices=USER_GENDER, default='')  
    bio = models.CharField(max_length=240, default='')
    
    def __str__(self):
        return f'{self.user.username} Profile'
        
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
        
    #     img = Image.open(self.image.path)
        
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)