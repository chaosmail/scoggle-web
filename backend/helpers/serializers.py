import json

from rest_framework import serializers, exceptions


class JSONSerializerField(serializers.Field):
    """Serializable JSON Field"""

    def to_representation(self, obj):
        
        return obj

    def to_internal_value(self, data):

        if isinstance(data, str):
            try:
                value = json.loads(data.replace("'", '"'))
            except ValueError:
                raise exceptions.ValidationError("Parsing Error. Invalid JSON <{}>".format(data))
        else:
            value = data

        if value is not None and not isinstance(value, dict) and not isinstance(value, list):
            raise exceptions.ValidationError("Invalid JSON <{}>".format(value))

        return value