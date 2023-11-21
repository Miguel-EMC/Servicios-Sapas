from django.db import models
from django.utils import timezone

class Category(models.Model):
    options = (
        ("draft", "Draft"),
        ("published", "Published"),
    )

    name = models.CharField(max_length=255, unique=True)
    thumbnail = models.CharField(max_length=500)
    description = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=options, default="published")
    
    def __str__(self) -> str:
        return self.name