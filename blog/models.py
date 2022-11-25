from django.db import models

class Blog(models.Model):
    Title = models.CharField(max_length=200)
    Date = models.DateField()
    Text = models.TextField()

    def __str__(self):
        return self.title