from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

class placex(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')


    def __str__(self):
        return self.name
