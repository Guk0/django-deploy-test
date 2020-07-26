from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField('date published')
    objects = models.Manager()

    def __str__(self):
        return self.title

    # 100번째 글자까지만 보여줌
    def summery(self):
        return self.content[:100]        