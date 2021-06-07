from django.db import models

# Create your models here.


class ToDo(models.Model):
    title = models.CharField(max_length=50)
    sub_title = models.CharField(max_length=200)
    due_date = models.DateField()

    def __str__(self):
        return "{0}.{1}".format(self.pk, self.title)
