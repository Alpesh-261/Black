from django.db import models
from django.contrib.auth.models import AbstractUser

class Yourdata(models.Model):
    end_year = models.CharField(max_length=100)
    intensity = models.CharField(max_length=100)
    sector = models.CharField(max_length=255)
    topic = models.CharField(max_length=255)
    insight = models.CharField(max_length=255)
    url = models.URLField(max_length=200)
    region = models.CharField(max_length=255)
    start_year = models.CharField(max_length=100)
    impact = models.CharField(max_length=255)
    added = models.DateTimeField(null=True, blank=True)
    published = models.DateTimeField(null=True, blank=True)
    country = models.CharField(max_length=255)
    relevance = models.CharField(max_length=100)
    pestle = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    title = models.TextField()
    likelihood = models.CharField(max_length=100)
    
    def __str__(self):
        return self.sector
