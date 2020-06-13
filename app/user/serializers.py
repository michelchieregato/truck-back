import re

from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.
    """

    PASSWORD_VERIFICATION = '^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])'

    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'name']
        extra_kwargs = {
            'password': {
                'write_only': True,
                'min_length': 6
            }
        }

    def validate_password(self, value):
        password_match = re.compile(self.PASSWORD_VERIFICATION)
        if password_match.search(value):
            return value
        raise serializers.ValidationError('Your password must match the security requirements')

    def create(self, validated_data):
        """
        Create a new user. Overwrites default ModelSerializer default creation
        (the default creation uses only the objects.create instead of create_user).
        """
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """
        Update a user, setting the password correctly and return it
        """
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class AuthTokenSerializer(serializers.Serializer):
    """
    Serializer for the user authentication object.
    """
    email = serializers.CharField()
    password = serializers.CharField(style={
        'input_type': 'password'
    }, trim_whitespace=False)

    def validate(self, attrs):
        """
        Validate and authenticate the user.
        Args:
            attrs: Dictionary containing both email and password attributes.
        Returns:
            attrs: The attrs provided, with now the user information.
        Raises:
            ValidationError if the user is unable to be authenticated.
        """
        credentials = {
            "username": attrs.get('email'),
            "password": attrs.get('password')
        }

        user = authenticate(**credentials)

        if not user:
            raise serializers.ValidationError(_('Unable to authenticate. Check your email and password.'),
                                              code='authentication')
        attrs['user'] = user
        return attrs