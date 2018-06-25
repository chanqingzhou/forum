from django.db import models

class Faculty(models.Model):
    faculty_text=models.CharField(max_length=40)
    def __str__(self):
        return self.faculty_text

class Module(models.Model):
    module_text=models.CharField(max_length=10)
    faculty= models.ForeignKey(Faculty, on_delete=models.CASCADE)
    def __str__(self):
        return self.module_text

class ModuleYear(models.Model):
    year= models.CharField(max_length=10)
    module=models.ForeignKey(Module, on_delete=models.CASCADE)
    def __str__(self):
        return self.year

class Question(models.Model):
    question_text=models.CharField(max_length=200)
    moduleYear=models.ForeignKey(ModuleYear,on_delete= models.CASCADE)
    def __str__(self):
        return self.question_text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=1000)
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)
    def __str__(self):
        return self.answer_text

class Votedby(models.Model):
    user_voted=models.CharField(max_length=40)
    answer= models.ForeignKey(Answer,on_delete=models.CASCADE)
    def __str__(self):
        return self.user_voted