from django.db import models
from django.contrib import admin
class footballplayers(models.Model):
    Name=models.CharField(max_length=20)
    DOB=models.DateField()
    Height=models.IntegerField()
    Address=models.CharField(max_length=100)
    MobileNO=models.IntegerField()
class footballplayersAdmin(admin.ModelAdmin):
   list_display=["Name","DOB","Height","Address","MobileNO"]
