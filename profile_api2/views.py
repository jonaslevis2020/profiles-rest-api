


from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from profile_api2 import permissions
from profile_api2 import models
from profile_api2.models import UserProfile
from profile_api2.serializers import HelloSerializer, UserProfileSerializer


class HelloApiView(APIView):
    """ApiView test"""

    serializer_class = HelloSerializer

    def get(self, request, format=None):
        """Returns a list of ApiView features"""
        api_view = [
            'Uses http methods as function (get, post, put, patch, delete)',
            'Is similar to a traditional django view',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs'
        ]
        users = UserProfile.objects.all()
        usernames = []
        emails = []
        for user in users:
            usernames.append(user.get_full_name())
            emails.append(user.__str__())
        return Response({'message':'Hello, world!', 'api_view':api_view, 'users':usernames, 'emails':emails})

    def post(self, request):
        """Create a hello message with our name"""
        serialized_data = self.serializer_class(data = request.data)

        if serialized_data.is_valid():
            name = serialized_data.validated_data.get('name')
            email = serialized_data.validated_data.get('email')
            message = f'Hello, {name}'
            email = f'Your email is {email}'

            return Response({'message':message, 'info':email}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(
                serialized_data.errors,
                status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle updating and object"""

        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""

        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""

        return Response({'method': 'DELETE'})



class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    serializer_class = HelloSerializer

    def list(self, request):
        """Return a list of objects"""

        return Response({'http_method': 'GET'})

    def create(self, request):
        """Create an object"""

        serialized_data = self.serializer_class(data=request.data)
        if serialized_data.is_valid():
            print(serialized_data.validated_data.get('name'))

        return Response({'http_method': 'PUT'})

    def update(self, request, pk=None):
        """Hanlde updating an object"""

        return Response({'http_method': 'UPDATE'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""

        return Response({'http_method': 'DELETE'})


class UserProfilesViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""

    serializer_class = UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)#remember the comma to make it a tuple
    permission_classes = (permissions.UpdateOwnProfile,)#don't forget the comma
    filter_backends = (filters.SearchFilter,)#the comma again
    search_fields = ('id','name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES