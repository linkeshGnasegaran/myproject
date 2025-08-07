from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add extra fields if needed
    pass
    user_type = models.CharField(max_length=20, choices=[
        ('admin', 'Admin'),
        ('cashier', 'Cashier'),
        ('manager', 'Manager')
    ])
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name