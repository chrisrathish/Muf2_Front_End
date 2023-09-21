from django.db import models

class CompletedJob(models.Model):
    name = models.CharField(max_length=100)
    result = models.FileField(upload_to='results/')
    completed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name