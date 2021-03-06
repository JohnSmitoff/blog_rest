from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.


class Question(models.Model):
    author = models.CharField(default="Anonymous", max_length=200)
    question = models.TextField()
    question_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.author} asked | {self.question}"


class Answer(models.Model):
    author = models.CharField(max_length=200, default="Anonymous")
    content = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    answer_time = models.DateTimeField(default=timezone.now)
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="answers"
    )

    def __str__(self):
        return f"{self.author} answered - {self.content} | {self.question} | likes:{self.likes} dislikes:{self.dislikes}"
