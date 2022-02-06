import graphene
from core.graphql import inputs
from core.models import Insurance


class UpdateInsurance(graphene.Mutation):
    ok = graphene.Boolean()
    success = graphene.String()
    error = graphene.String()

    class Arguments:
        policy_id = graphene.ID(required=True)
        fuel = graphene.String()
        vehicle_segment = graphene.String()
        premium = graphene.Decimal()
        bodily_injury = graphene.Boolean()
        personal_injury_protection = graphene.Boolean()
        property_damage_liability = graphene.Boolean()
        collision = graphene.Boolean()
        comprehensive = graphene.Boolean()

    @staticmethod
    def mutate(self, info, **kwargs):
        try:
            insurance = Insurance.objects.get(policy_id=kwargs["policy_id"])
            if "fuel" in kwargs:
                insurance.fuel = kwargs["fuel"]
            if "vehicle_segment" in kwargs:
                insurance.vehicle_segment = kwargs["vehicle_segment"]
            if "premium" in kwargs:
                if kwargs["premium"] > 1000000:
                    return {"ok": False, "error": "Premium amount is greater than 1 Million"}
                else:
                    insurance.premium = kwargs["premium"]
            if "bodily_injury" in kwargs:
                insurance.bodily_injury = kwargs["bodily_injury"]
            if "personal_injury_protection" in kwargs:
                insurance.personal_injury_protection = kwargs["personal_injury_protection"]
            if "property_damage_liability" in kwargs:
                insurance.property_damage_liability = kwargs["property_damage_liability"]
            if "collision" in kwargs:
                insurance.collision = kwargs["collision"]
            if "comprehensive" in kwargs:
                insurance.comprehensive = kwargs["comprehensive"]

            insurance.save()

        except Insurance.DoesNotExist:
            return {"ok": False, "error": "Record not found"}

        except Exception as e:
            return {"ok": False, "error": str(e)}

        return {"ok": True, "success": "Details updated successfully"}


class Mutation(graphene.ObjectType):
    update_insurance = UpdateInsurance.Field()
