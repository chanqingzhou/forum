from django.db import models
from django.contrib.auth.models import User
class Faculty(models.Model):
    faculty_text=models.CharField(max_length=40)
    def __str__(self):
        return self.faculty_text

class Module(models.Model):
    module_text=models.CharField(max_length=50)
    module_code=models.CharField(max_length=10)
    faculty= models.ForeignKey(Faculty, on_delete=models.CASCADE)
    def __str__(self):
        return self.module_code

class ModuleYear(models.Model):
    year= models.CharField(max_length=10)
    module=models.ForeignKey(Module, on_delete=models.CASCADE)
    def __str__(self):
        return self.year

class Answer(models.Model):
    year = models.ForeignKey(ModuleYear, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=1000)
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)
    def __str__(self):
        return self.answer_text

class AnswerFile(models.Model):
    title =models.CharField(max_length=100)
    answer= models.ForeignKey(Answer,on_delete=models.CASCADE,blank=True)
    file= models.FileField(upload_to='uploads/')


class Votedby(models.Model):
    user_voted=models.CharField(max_length=40)
    answer= models.ForeignKey(Answer,on_delete=models.CASCADE)
    def __str__(self):
        return self.user_voted

class Comments(models.Model):
    user=models.CharField(max_length=40)
    answer= models.ForeignKey(Answer,on_delete=models.CASCADE)
    text= models.CharField(max_length=2000)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.user