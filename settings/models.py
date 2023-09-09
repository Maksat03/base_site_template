from django.db import models


class Slide(models.Model):
    image = models.ImageField(upload_to="slide_images/")
    link = models.CharField(max_length=500, default="/")
