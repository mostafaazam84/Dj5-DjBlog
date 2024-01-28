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