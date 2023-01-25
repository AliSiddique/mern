from django.db import models
from user.models import Profile
from django.contrib.auth.models import User
from django.db.models.signals import pre_save

class University(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField()
    slug = models.SlugField()

    def __str__(self):
        return self.name


class Accomodation(models.Model):
    uni = models.ForeignKey(University,on_delete=models.CASCADE,related_name='unis')
    slug = models.SlugField()

    name = models.CharField(max_length=100)
    image = models.ImageField(blank=True,null=True)    
    def __str__(self):
        return self.name

class Choices(models.Model):
  name = models.CharField(max_length=30)
  def __str__(self):
        return self.name
class Post(models.Model):
    accom = models.ForeignKey(Accomodation,on_delete=models.CASCADE,related_name='accom')
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    image = models.ImageField(blank=True,null=True)
    image = models.ImageField(blank=True,null=True)
    image = models.ImageField(blank=True,null=True)
    image = models.ImageField(blank=True,null=True)
    image = models.ImageField(blank=True,null=True)
    video = models.FileField(blank=True,null=True)
    description = models.TextField(max_length=500,blank=True,null=True)
    rating_room =  models.FloatField(default=0)
    rating_house =  models.FloatField(default=0)
    rating_bath =  models.FloatField(default=0)
    rating_location =  models.FloatField(default=0)
    average = models.FloatField(default=0)
    likes = models.ManyToManyField(
        User, related_name='like', default=None, blank=True)
    like_count = models.BigIntegerField(default='0')
    choices = models.ManyToManyField(Choices,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.profile.user.username



def calculate_avg(sender,instance,*args,**kwargs):
        post = instance
        average =  float((post.rating_room + post.rating_house + post.rating_bath + post.rating_location) / 4)
        post.average = "{:.1f}".format(average)



pre_save.connect(calculate_avg,sender=Post)               