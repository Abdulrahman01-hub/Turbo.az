from django.db import models
from django.contrib.auth.models import User

class Car(models.Model):
    CONDITION_CHOICES = [
        ('new', 'New'),
        ('used', 'Used'),
    ]

    TRANSMISSION_CHOICES = [
        ('manual', 'Manual'),
        ('automatic', 'Automatic'),
    ]

    FUEL_CHOICES = [
        ('gasoline', 'Gasoline'),
        ('diesel', 'Diesel'),
        ('electric', 'Electric'),
        ('hybrid', 'Hybrid'),
    ]

    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    mileage = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=50)
    condition = models.CharField(max_length=10, choices=CONDITION_CHOICES, default='used')
    transmission = models.CharField(max_length=10, choices=TRANSMISSION_CHOICES, default='manual')
    fuel_type = models.CharField(max_length=10, choices=FUEL_CHOICES, default='gasoline')
    description = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cars')
    city = models.CharField(max_length=100, default='Baku')
    image = models.ImageField(upload_to='car_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year}) by {self.seller.username}"
