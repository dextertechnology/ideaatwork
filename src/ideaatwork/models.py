from django.db import models
from django.contrib.auth.models import User


class Idea(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=500)
    suggested_by = models.ForeignKey(User, on_delete=models.CASCADE)
    published_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class Vote(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
    voted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    voted_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.idea}-{self.voted_by}"

    class Meta:
        unique_together = ("idea", "voted_by")