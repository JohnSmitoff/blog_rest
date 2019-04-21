from django.db import models

# Create your models here.


class Question(models.Model):
    author = models.CharField(default="Anonymous", max_length=200)
    question = models.TextField()
    question_time = models.TimeField()

    def __str__(self):
        return f"{self.author} asked | {self.question}"


class Answer(models.Model):
    author = models.CharField(max_length=200, default="Anonymous")
    content = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    answer_time = models.TimeField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author} answered - {self.content} | {self.question} | likes:{self.likes} dislikes:{self.dislikes}"
