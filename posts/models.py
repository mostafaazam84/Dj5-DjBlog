from django.utils import timezone
from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User


# Create your models here.

'''
   post:
    - title
    - content
    - publish_data
    - author
    - image
    - tags
    - category
    - comments
'''
class Post(models.Model):
    author = models.ForeignKey(User,related_name='post_author',on_delete=models.CASCADE)
    title =  models.CharField(max_length=100)
    content = models.TextField()
    draft = models.BooleanField(default= True)
    publish_date = models.DateTimeField(default=timezone.now)
    
    # create time auto
    publish_date2 = models.DateTimeField(auto_now=True) 
    
    tags = TaggableManager()
    image = models.ImageField(upload_to='post')
    
    
    def __str__(self):
        return self.title
        