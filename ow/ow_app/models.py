from django.db import models

# Create your models here.
class Category(models.Model):
    short_name = models.CharField(max_length=20)
    about = models.CharField(max_length=50)

    def __str__(self):
        return self.short_name

class Service(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100,null=False, blank=False )
    text = models.TextField(max_length=1000)

    def __str__(self):
        return self.title
