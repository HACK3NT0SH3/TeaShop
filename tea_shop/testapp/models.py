from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100, blank=False)
    price = models.IntegerField()
    kind = models.CharField(max_length=100, blank=False)
    taste = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    plantation = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=500)
    primary_notes = models.CharField(max_length=100)
    rating = models.CharField(max_length=5)
    reviews = models.IntegerField(default=0)

class Review(models.Model):
    rating = models.IntegerField()
    text = models.CharField(max_length=1000)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

class Cart(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    delivery_address = models.CharField(max_length=150)
    payment_method = models.CharField(max_length=100)

class Order(models.Model):
    cart_info = models.ForeignKey(Cart, on_delete=models.CASCADE)
    total_cost = models.IntegerField()

class Catalog(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
