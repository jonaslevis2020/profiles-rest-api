


from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response



class HelloApiView(APIView):
    """ApiView test"""

    def get(self, request, format=JsonResponse):
        """Returns a list of ApiView features"""
        api_view = [
            'Uses http methods as function (get, post, put, patch, delete)',
            'Is similar to a traditional django view',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs'
        ]
        return Response({'message':'Hello, world!', 'api_view':api_view})