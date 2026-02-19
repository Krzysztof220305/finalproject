from django.db import models

class Item(models.Model):
    """
    Model representing an item in the inventory.
    Stores name, description, and an image hosted on Azure Blob Storage.
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    image = models.ImageField(upload_to='items/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name