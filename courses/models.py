from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=0)
    duration = models.CharField(max_length=15, null=True, blank=True)
    participants = models.DecimalField(max_digits=1, decimal_places=0)
    level = models.CharField(max_length=15, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
