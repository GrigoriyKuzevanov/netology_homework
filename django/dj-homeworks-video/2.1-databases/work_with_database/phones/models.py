from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=40)
    image = models.CharField(max_length=400)
    release_date = models.CharField(max_length=40)
    lte_exists = models.BooleanField(null=True)
    slug = models.SlugField(max_length=50, null=True)

