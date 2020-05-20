from django.db import models

#from blogapp import blogs
# Create your models here.
class uploadForm(models.Model):
    title=models.CharField(max_length=20)
    description=models.CharField(max_length=200)
    pic=models.FileField(upload_to='images/')
    author=models.CharField(max_length=20)
    upload_date=models.DateTimeField(auto_now_add=True)
    #upload_date=models.DateTimeField(default=datetime.now)
