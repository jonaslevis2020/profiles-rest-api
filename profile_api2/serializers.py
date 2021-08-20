




from rest_framework import fields, serializers
from profile_api2 import models

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our ApiView"""

    name = serializers.CharField(max_length = 20)
    email = serializers.EmailField(max_length = 50)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'name', 'email', 'password', 'is_active', 'is_staff', 'is_superuser')
        extra_kwargs = {
            'password':{
                'write_only':True,
                'style':{
                    'input_type':'password'
                }
            },
            'email':{
                'style':{
                    'input_type':'email'
                }
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""

        user = models.UserProfile.objects.create_user(
            name = validated_data['name'],
            email = validated_data['email'],
            password = validated_data['password'],

        )

        return user