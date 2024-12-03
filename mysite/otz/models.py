from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField( max_length=50)
    pub_date = models.DateField(("date published"), auto_now=False, auto_now_add=False)

class Choice(models.Model):
    question = models.ForeignKey(Question,  on_delete=models.CASCADE)
    choice_text = models.CharField( max_length=50)
    votes = models.IntegerField(default= 0)   

 
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Choice_detail", kwargs={"pk": self.pk})
