from django.utils import timezone
from django.db import models

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
    title =  models.CharField(max_length=100)
    content = models.TextField()
    draft = models.BooleanField(default= True)
    publish_date = models.DateTimeField(default=timezone.now)
    
    # create time auto
    publish_date2 = models.DateTimeField(auto_now=True) 
    
    
    def __str__(self):
        return self.title
        