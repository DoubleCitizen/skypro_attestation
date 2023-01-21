from rest_framework import serializers

from core.models import Factory, RetailChain, IndividualEntrepreneur, Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"


class FactorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Factory
        fields = "__all__"


class RetailChainSerializer(serializers.ModelSerializer):
    class Meta:
        model = RetailChain
        fields = "__all__"
        read_only_fields = ("debt",)


class IndividualEntrepreneurSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndividualEntrepreneur
        fields = "__all__"
        read_only_fields = ("debt",)
