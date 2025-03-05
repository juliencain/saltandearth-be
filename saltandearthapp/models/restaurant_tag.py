from django.db import models
from .restaurant import Restaurant
from saltandearthapp.models.tag import Tag


class RestaurantTag(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="restaurant_tags")
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name="restaurants")
