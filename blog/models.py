from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

    
class User(AbstractUser):
    username = models.CharField(max_length = 150, blank = True, null = True, unique = True)
    phone_no = models.CharField(max_length = 10, blank = True, null = True)
    email = models.CharField(max_length= 100, blank = True, null = True)
    city=models.CharField(max_length = 150, blank = True, null = True)
    state=models.CharField(max_length = 150, blank = True, null = True)
    country=models.CharField(max_length = 150, blank = True, null = True)
    # image = models.ImageField(upload_to='image/', blank=True, null = True)
 
    def __str__(self):
        return self.username


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.title