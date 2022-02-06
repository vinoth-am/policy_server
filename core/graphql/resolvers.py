from django.db.models import Q
import datetime

from core.utils import fomat_date


class SearchListResolver:
    def __init__(self, model):
        self.model = model

    def __call__(self, info, source, search):
        if search.strip() != "":
            filters = (
                    Q(policy_id__icontains=search) |
                    Q(customer_id__icontains=search)
            )
            qs = self.model.objects.filter(filters)
            return qs


class ListResolver:
    def __init__(self, model):
        self.model = model

    def __call__(self, info, source, **kwargs):
        if "region" in kwargs:
            qs = self.model.objects.filter(customer_region=kwargs["region"])
            data = {}
            for _, c in enumerate(qs):
                format_date = fomat_date(c.date_purchase)
                if not format_date in data:
                    data[format_date] = 1
                else:
                    data[format_date] += 1
            return {"insurance_count": data}
