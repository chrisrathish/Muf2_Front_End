from django.db import models

class Job(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    progress = models.IntegerField(default=0)

    def __str__(self):
        return self.name
