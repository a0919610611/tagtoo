from django.db import models


# Create your models here.
class Advertiser(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    #        title=models.CharField(max_length=1000,null=True)
    product_key = models.CharField(max_length=255, unique=True, null=True)
    price = models.IntegerField(null=True)
    store_price = models.IntegerField(null=True)
    advertiser = models.ForeignKey('Advertiser', on_delete=models.CASCADE, null=True)
    Class = models.CharField(max_length=255, null=True)
    update_time = models.DateTimeField(null=True)


class Transcation(models.Model):
    user = models.CharField(max_length=255, null=True)
    value = models.IntegerField(null=True)
    currency = models.CharField(max_length=255, null=True)
    num_items = models.CharField(max_length=255, null=True)
    content_ids = models.CharField(max_length=255, null=True)
    advertiser = models.ForeignKey('Advertiser', on_delete=models.CASCADE, null=True)
    purchase_time = models.DateTimeField(null=True)
    click_time_last = models.DateTimeField(null=True)
    click_time_7_days = models.DateTimeField(null=True)
    click_time_30_days = models.DateTimeField(null=True)
    ip = models.CharField(max_length=255, null=True)
    user_agent = models.CharField(max_length=255, null=True)
