from django.db import models

class Image(models.Model):
    name = models.CharField(max_length=32,default='image')
    desc = models.TextField(default="image desc")
    fileName = models.CharField(max_length=32)
    path = models.CharField(max_length= 150)
    size = models.IntegerField()
    type = models.CharField(max_length=15)
    saveDate = models.DateField(auto_now=True)


