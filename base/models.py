from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Link(models.Model):
    youtube = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)

    def __str__(self):
        return str('social_link_'+str(self.id))

class Advocate(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)    
    name = models.CharField(max_length=200, null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True)
    short_bio = models.CharField(max_length=1000, null=True, blank=True)
    long_bio = models.TextField(null=True, blank=True)
    advocate_years_exp = models.IntegerField(null=True, blank=True, default=0)
    links = models.OneToOneField(Link, on_delete=models.SET_NULL, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.name



class Company(models.Model):
    name =  models.CharField(max_length=200, null=True, blank=True)
    logo = models.ImageField(null=True, blank=True)
    href = models.URLField(blank=True, null=True)
    summary = models.TextField(null=True, blank=True)
    advocates = models.ManyToManyField(Advocate, blank=True)
    

    class Meta:
        verbose_name_plural = 'Companies'

    def __str__(self):
        return str(self.name)



