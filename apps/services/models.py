from django.db import models
import uuid
from django.utils import timezone

# Create your models here.
class Service(models.Model):
    
    options = (
        ("draft", "Draft"),
        ("published", "Published"),
    )

    service_uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    name_service = models.CharField(max_length=255)
    # category = models.ForeignKey(Category, on_delete=models.PROTECT)
    description = models.TextField()
    materials = models.TextField()
    thumbnail = models.CharField(max_length=500)
    published = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=options, default="published")
    
    # Reltation
    # create_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    # spa_id = models.ForeignKey(Spa, on_delete=models.PROTECT, null=True)
    
    def __str__(self) -> str:
        return self.name_service