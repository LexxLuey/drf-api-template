from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "is_agent",
            "is_artist",
            "is_subscribed",
        ]
