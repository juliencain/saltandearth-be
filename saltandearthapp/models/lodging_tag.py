from django.db import models
from .lodging import Lodging
from .tag import Tag

class LodgingTag(models.Model):
    lodging_id = models.ForeignKey(Lodging, on_delete=models.CASCADE, related_name="lodging_tags")
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name="lodgings")

    
    