from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=225)
    price = models.IntegerField(
        null=True,
        blank=True,
        validators=[
            MaxValueValidator(200000),
            MinValueValidator(500)
        ]
    )
    date_of_issue = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='product_img/', null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pk}: {self.title}"

class Category(models.Model):
    category = models.CharField(db_index=True, max_length=150)

    def __str__(self):
        return f"{self.pk}: {self.category}"
