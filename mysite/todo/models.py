from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField("授業名", max_length=30)
<<<<<<< HEAD
    assignment = models.TextField("課題", blank=True)
    description = models.TextField("詳細", blank=True)
=======
    description = models.TextField("提出物", blank=True)
>>>>>>> 04f7a03bae29b79cf4e1a17a3ab241a394bc02cb
    deadline = models.DateField("締め切り")
    
    def __str__(self):
        return self.title
    