from django.db import models

class Blog(models.Model):
    Title = models.CharField(max_length=20)
    Date = models.DateField(auto_now=True)
    Text = models.CharField(max_length=250)