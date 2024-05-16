from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=150)
    image_url = models.URLField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    url = models.URLField()

    #defining a sorting order. sorting is done on the price field.	
    class Meta:
        ordering = ['-price']
        #define database index for price field.(optional) - it  could comprise one or multiple fields, in ascending or descending
        #order, or functional expressions and database functions. NOT SUPPORTED IN MYSQL DATABASE.
        indexes = [
            models.Index(fields=['-price']),
            ]

    def __str__(self):
        return self.name