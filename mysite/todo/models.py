from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField("授業名", max_length=30)
    assignment = models.TextField("課題", blank=True)
    description = models.TextField("詳細", blank=True)
    deadline = models.DateField("締め切り")

    def __str__(self):
        return self.title
