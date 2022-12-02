from rest_framework import serializers

class AuthorListingField(serializers.RelatedField):
    def to_representation(self, instance):
        return instance.last_name