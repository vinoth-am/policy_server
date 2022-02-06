from django.contrib import admin
from core.models import Insurance


@admin.register(Insurance)
class Insurance(admin.ModelAdmin):
    list_display = (
        "id", "policy_id", "date_purchase", "customer_id", "fuel", "vehicle_segment", "premium", "bodily_injury",
        "personal_injury_protection", "property_damage_liability", "collision", "comprehensive"
        ,'customer_gender', 'customer_income_group', "customer_region", "customer_marital_status")

    list_filter = ('fuel', 'vehicle_segment')
