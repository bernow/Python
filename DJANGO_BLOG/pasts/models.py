from django.db import models

class Past(models.Model):
    name = models.CharField(max_length=20)
    past_job = models.TextField()

    def __str__(self):
        return self.name