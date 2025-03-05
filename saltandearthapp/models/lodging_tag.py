from django.db import models
from .lodging import Lodging
from saltandearthapp.models.tag import Tag


class LodgingTag(models.Model):
    lodging = models.ForeignKey(Lodging, on_delete=models.CASCADE, related_name="lodging_tags")
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name="lodgings")

    
    