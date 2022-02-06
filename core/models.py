from django.db import models


class Insurance(models.Model):
    id = models.AutoField(primary_key=True)
    policy_id = models.BigIntegerField(null=False)
    date_purchase = models.DateField(null=False)
    customer_id = models.BigIntegerField(null=False)
    fuel = models.CharField(max_length=100, null=False)
    vehicle_segment = models.CharField(max_length=100, null=False)
    premium = models.DecimalField(null=False, decimal_places=2, max_digits=9)
    bodily_injury = models.BooleanField()
    personal_injury_protection = models.BooleanField()
    property_damage_liability = models.BooleanField()
    collision = models.BooleanField()
    comprehensive = models.BooleanField()
    customer_gender = models.CharField(null=False, max_length=100)
    customer_income_group = models.CharField(null=False, max_length=256)
    customer_region = models.CharField(null=False, max_length=100)
    customer_marital_status = models.BooleanField()
