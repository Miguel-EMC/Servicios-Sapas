from django.db import models
import uuid
from django.utils import timezone
from apps.categories.models import Category
from apps.spas.models import Spa
from apps.users.models import User

# Create your models here.
class Service(models.Model):
    
    options = (
        ("draft", "Draft"),
        ("published", "Published"),
    )

    service_uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    name_service = models.CharField(max_length=255)
    description = models.TextField()
    materials = models.TextField()
    thumbnail = models.CharField(max_length=500)
    status = models.CharField(max_length=10, choices=options, default="published")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)
    
    published = models.DateTimeField(default=timezone.now)
    spa_id = models.ForeignKey(Spa, on_delete=models.PROTECT, null=True)

    # Reltation
    create_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    
    def __str__(self) -> str:
        return self.name_service