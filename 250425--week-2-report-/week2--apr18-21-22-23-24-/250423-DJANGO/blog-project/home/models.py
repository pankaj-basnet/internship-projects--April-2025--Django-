from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):

    id = models.UUIDField(primary_key= True, default = uuid.uuid4, editable = False)
    title = models.CharField(max_length = 100)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    # is_active = models.BooleanField(default = True)
    updated_on = models.DateField(auto_now = True)
    created_on = models.DateField(auto_now_add = True)
