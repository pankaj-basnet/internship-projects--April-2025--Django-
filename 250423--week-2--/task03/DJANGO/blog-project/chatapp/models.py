
from django.db import models
import uuid
from django.contrib.auth.models import User

from home.models import Post
# Create your models here.

class Comment(models.Model):
    
    id = models.UUIDField(primary_key= True, default = uuid.uuid4, editable = False)
    sentences = models.TextField()
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.DO_NOTHING) # on_delete = models.DO_NOTHING required