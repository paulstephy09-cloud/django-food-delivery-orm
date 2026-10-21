from django.db import models


class FoodItem(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    restaurant = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    rating = models.FloatField()
    is_available = models.BooleanField(default=True)

    class Meta:
        db_table = 'food_delivery_fooditem'

    def __str__(self):
        return self.name
