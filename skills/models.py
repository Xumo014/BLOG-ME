from django.db import models

# Create your models here.

class Skills(models.Model):
    skill_name = models.CharField(max_length = 100)
    daraja = models.CharField(max_length = 3)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self) -> str:
        return self.skill_name
    

class Abouts(models.Model):
    title = models.CharField(max_length = 200)
    body = models.TextField()
    image = models.FileField(upload_to="post-images")

    def __str__(self) -> str:
        return self.title
