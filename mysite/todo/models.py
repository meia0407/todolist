from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField("授業名", max_length=30)
    deadline = models.DateField("締め切り")
    assignment = models.TextField("課題", blank=True, max_length=20)
    description = models.TextField("詳細", blank=True, max_length=20)

    def __str__(self):
        return self.title
