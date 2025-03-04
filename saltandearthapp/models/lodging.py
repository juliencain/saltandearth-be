from django.db import models
from .user import User
from .city import City

class Lodging(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lodging')
    uid = models.CharField(max_length=50)
    city_id = models.ForeignKey(City, on_delete=models.CASCADE, related_name='lodging_created')
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    description = models.CharField(max_length=280)
    image = models.URLField()
    link = models.URLField(blank=True, null=True)
