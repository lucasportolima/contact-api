from rest_framework import serializers

from .models import VarejaoContact


class VarejaoContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = VarejaoContact
        fields = '__all__'

    def validate_celular(self, cellphone):
        """ validate cell number """

        if len(cellphone) != 13:
            raise serializers.ValidationError(
                'Celular inválido! Utilize o formato: 5541979210400')
        return cellphone
