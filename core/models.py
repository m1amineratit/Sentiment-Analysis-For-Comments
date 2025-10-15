from django.db import models

# Create your models here.


class Comment(models.Model):
    text = models.CharField(max_length=50)
    sentiment = models.CharField(max_length=100)
    summary = models.CharField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text[:30]}, sentiment: {self.sentiment}"
    
