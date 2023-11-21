from django.db import models
from django.utils import timezone
import uuid
from apps.users.models import User

class Spa(models.Model):
    options = (
        ("draft", "Draft"),
        ("published", "Published"),
    )
    
    spa_uuid = models.UUIDField(default=uuid.uuid4, unique=True, blank=False)
    name = models.CharField(max_length=255, unique=True)
    thumbnail = models.CharField(max_length=500)
    description = models.TextField()
    address = models.CharField(max_length=255, null=True)
    published = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=options, default="published")
    
    person_spa_id = models.OneToOneField(User, on_delete=models.PROTECT, null=True)

    def __str__(self) -> str:
        return self.name