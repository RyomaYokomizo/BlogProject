from django.db import models
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100, null=False)
    text = models.TextField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
        