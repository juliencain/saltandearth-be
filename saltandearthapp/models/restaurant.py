from django.db import models
from .user import User
from .city import City

class Restaurant(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='restaurants')
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    image = models.URLField()
    city_id = models.ForeignKey(City, on_delete=models.CASCADE, related_name='restaurants_created')
    description = models.CharField(max_length=280)
    link = models.URLField(blank=True, null=True)
