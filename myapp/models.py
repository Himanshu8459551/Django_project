from django.db import models

# Create your models here.
class Member1(models.Model):
  def __str__(self):
    return self.firstname
  
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=300)
  rollno= models.IntegerField(null=True)
  #image = models.ImageField(default='default.jpg',upload_to='member_photo/')
  image = models.ImageField(upload_to='image')




  