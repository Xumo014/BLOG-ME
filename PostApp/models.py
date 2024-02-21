from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=500)
    body = models.TextField()
    image = models.FileField(upload_to="post-images")
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', related_name='tags', blank=True, null=True)

    class Meta:
        app_label = 'PostApp'
        ordering = ['-created']

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Coments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    website = models.CharField(max_length=150, blank=True, null=True)
    msg = models.TextField()

    def __str__(self):
        return self.name