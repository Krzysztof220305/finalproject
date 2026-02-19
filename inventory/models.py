from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) # Tego brakowało
    image = models.ImageField(upload_to='items/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name