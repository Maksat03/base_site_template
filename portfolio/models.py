from django.db import models


class Portfolio(models.Model):
    categories = models.ManyToManyField("product.ProductCategory")
    products = models.ManyToManyField("product.Product")
    name = models.CharField(max_length=255)
    poster = models.ImageField(upload_to="portfolio_posters/")
    description = models.TextField()
    feedback = None  # TODO: think out


class PortfolioImage(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="portfolio_images/")
