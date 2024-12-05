from django.db import models

# Yaha pe models define karna hai first step after editing settings.py setha

class Kar(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='car_images/')  # Defines the folder for image uploads

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
