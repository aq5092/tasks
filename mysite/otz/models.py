from django.db import models

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
        return super().__str__()


class Question(models.Model):
    question_text = models.CharField( max_length=50)
    pub_date = models.DateField(("date published"), auto_now=False, auto_now_add=False)

class Choice(models.Model):
    question = models.ForeignKey(Question,  on_delete=models.CASCADE)
    choice_text = models.CharField( max_length=50)
    votes = models.IntegerField(default= 0)   

 
    def __str__(self):
        return self.name
