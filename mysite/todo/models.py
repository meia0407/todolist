from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField("授業名", max_length=30)
    description = models.TextField("提出物", blank=True)
    deadline = models.DateField("締め切り")
    
    def __str__(self):
        return self.title
    