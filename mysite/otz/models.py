from django.db import models
from import_export import resources
from django.utils import formats
""" 
34.217.184.131
44.234.233.60
52.32.132.51 """
# Create your models here.


class Tasks(models.Model):
    mavzu = models.CharField(max_length= 500)
    nomer = models.CharField(max_length=150)
    sana = models.DateTimeField(auto_created=True)
    muddat = models.DateTimeField(auto_created=True)
    javobgar= models.CharField(max_length=200)
    topshiriq_turi= models.CharField(max_length=200)
    topshiriq_kimdan = models.CharField(max_length=200)
    status = models.CharField(max_length=500, blank=True)
    natijasi = models.CharField(max_length=500, blank=True  )

    def format_datetime(self):
        return formats.date_format(self.sana, "d.M.Y")


    def __str__(self) -> str:
        return self.topshiriq_turi


