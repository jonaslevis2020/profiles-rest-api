




from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our ApiView"""

    name = serializers.CharField(max_length = 20)
    email = serializers.EmailField(max_length = 50)