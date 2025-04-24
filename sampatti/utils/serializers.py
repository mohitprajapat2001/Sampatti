from rest_framework.serializers import ModelSerializer, ValidationError
from utils.constants import ValidationErrors


class CustomForeignKeySerializer(ModelSerializer):
    """
    Custom Foreign Key Serializer to handle the foreign key relationships
    in the serializers.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if fields := kwargs.get("fields"):
            for field in fields:
                if field not in self.fields:
                    self.fields.pop(field)

    def validate(self, attrs):
        attrs = super().validate(attrs)
        fields = self.Meta.model._meta.fields
        errors = {}
        for field in fields:
            if (
                field.is_relation
                and field.many_to_one
                and field.null is False
                and field.blank is False
            ):
                if not self.initial_data.get(field.column):
                    errors[field.name] = ValidationErrors.REQUIRED % field.name.title()
                else:
                    if value := self.initial_data.get(field.column):
                        if field.related_model.objects.filter(id=value).exists():
                            attrs[field.column] = value
                        else:
                            errors[field.name] = (
                                ValidationErrors.NOT_FOUND % field.name.title()
                            )
        if errors:
            raise ValidationError(errors)
        return attrs
