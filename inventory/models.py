from django.db import models

# Create your models here.
class inventory(models.Model):
    product_name=models.CharField(max_length=60)
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.product_name
