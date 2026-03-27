from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255) # [cite: 2]

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }

class Product(models.Model):
    name = models.CharField(max_length=255) # [cite: 2]
    price = models.FloatField() # [cite: 2]
    description = models.TextField() # [cite: 2]
    count = models.IntegerField() # [cite: 2]
    is_active = models.BooleanField(default=True) # [cite: 2]
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products') # [cite: 2]

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'count': self.count,
            'is_active': self.is_active,
            'category_id': self.category.id
        }
