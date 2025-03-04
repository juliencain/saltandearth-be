from django.db import models
from .restaurant import Restaurant
from .tag import Tag

class RestaurantTag(models.Model):
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="restaurant_tags")
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name="restaurants")
