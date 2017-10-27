from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey('auth.User')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

# API REST - JSON
# Informações -> JSON
# Modelos -> JSON
# JSON -> Modelos
