from django.db import models
""" 
34.217.184.131
44.234.233.60
52.32.132.51 """
# Create your models here.
class Tasks(models.Model):
    mavzu = models.CharField(max_length= 150)
    nomer = models.CharField(max_length=15)
    sana = models.DateField(auto_created=True)
    muddat = models.DateField()
    javobgar= models.CharField(max_length=20)
    topshiriq_turi= models.CharField(max_length=20)
    topshiriq_kimdan = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    natijasi = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.topshiriq_turi


