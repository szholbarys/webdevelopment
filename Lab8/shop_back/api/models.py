from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(default=0)
    description = models.TextField(default='')
    count = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

    def to_json(self):
        return {
            'id' : self.id,
            'name':self.name,
            'description' : self.description,
            'count': self.count,
            'is_active': self.is_active,
            'price': self.price,
            'category': self.category_id
        }
    
