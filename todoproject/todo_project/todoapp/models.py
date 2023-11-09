from django.db import models

# Create your models here.
class task(models.Model):
    taskname=models.CharField(max_length=250)
    taskpriority=models.IntegerField()
    taskdate=models.DateField()
    def __str__(self):
        return self.taskname

