# D:\GROW_CTS\Django-React-Full-Stack-App-main\backend\blog\models.py

from django.db import models
import uuid

from api.models import User

from django.utils.text import slugify
from django.urls import reverse
from django.conf import settings


class Tag(models.Model):
    
    id = models.UUIDField(
        primary_key = True, 
        default = uuid.uuid4,
        editable = False,
    )
    name = models.CharField(
        max_length = 50, 
        unique = True,
    )
    
    def __str__(self) -> str:
        return f"{self.name}"
    

class Post(models.Model):

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    id = models.UUIDField(
        primary_key = True, 
        default = uuid.uuid4,
        editable = False,
    )
    title = models.CharField(
        max_length = 100,
    )
    slug = models.SlugField(
        max_length = 255,
        unique = True,
        blank= True,
    )
    content = models.TextField(
        max_length = 500,
    )
    author = models.ForeignKey(
        User, 
        on_delete = models.DO_NOTHING,
        verbose_name = "Auther",
        related_name = "posts",
    )
    updated_at = models.DateTimeField(
        auto_now = True,
    )
    created_at = models.DateTimeField(
        auto_now_add = True,
    )
    status = models.CharField(
        max_length = 10,
        choices = STATUS_CHOICES,
        default = 'draft'
    )
    cover_image = models.ImageField(
        upload_to= 'covers/',
        blank= True,
        null= True,
    )
    tags = models.ManyToManyField(
        Tag, 
        blank= True
    )
    likes_count = models.IntegerField(
        default = 0,

    )
    is_draft = models.BooleanField(
        default = True,
    )


    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("blog:post-detail", kwargs={"slug": self.slug})
    

class Comment(models.Model):
    
    id = models.UUIDField(
        primary_key= True, 
        default = uuid.uuid4, 
        editable = False
    )
    sentences = models.TextField()
    post = models.ForeignKey(
        Post, 
        on_delete = models.CASCADE,
        verbose_name = "Post",
        related_name = "comments",
    )
    user = models.ForeignKey(
        User, 
        on_delete = models.DO_NOTHING,
        verbose_name = "User",
        related_name = "comments",
    ) # on_delete = models.DO_NOTHING required
    created_at = models.DateTimeField(
        auto_now_add = True,
    )
    
    #
    is_approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        return f'id : {(str(self.id))[:5]} -> {(self.sentences)[:15]}'


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)

    def __str__(self):
        return f"Like by {self.user} on {self.post.title}"
    

from django.contrib.auth.models import Group


class GroupProfile(models.Model):
    group = models.OneToOneField(Group, on_delete=models.CASCADE, related_name='profile')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.group.name
