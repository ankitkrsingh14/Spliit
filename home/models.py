from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Group(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255,blank=True,null=True,unique=True)
    is_admin = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

class HistoryMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    amount = models.IntegerField(blank=True,null=True,default=0)
    desc = models.CharField(max_length=255,blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True,blank=True,null=True)

    def __str__(self):
        return str(self.user)


class Member(models.Model):
    group = models.OneToOneField(Group, on_delete=models.CASCADE) 
    user = models.OneToOneField(User, on_delete=models.CASCADE) 

    def __str__(self):
        return str(self.group)