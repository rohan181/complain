from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class comaplain(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    content = models.TextField()
    assign = models.ForeignKey(User, null=True, related_name='assignee',on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)
    status_choices = [
        (1, 'Pending'),
        (2, 'Solved')
    ]
    status = models.IntegerField(choices=status_choices, default=1)
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title



class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    content = models.TextField()
    post = models.ForeignKey(comaplain, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Comment by {}'.format(self.name)       