from django.db import models

# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200) # tiap database harus punya max length biar uniform tiap tablenya
    #job_title = models.CharField(max_length=40)