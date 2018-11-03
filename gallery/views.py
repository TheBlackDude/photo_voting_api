from rest_framework import permissions, viewsets, status, views
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import Image
from .serializers import ImageSerializer


class ImageViewSet(viewsets.ModelViewSet):
    """
    API endpoint for creating and listing Images
    """
    queryset = Image.objects.order_by('-created_at')
    serializer_class = ImageSerializer

    def get_owner(self):
        # lookup user by their token and return True and the user
        # if token doesn't exist return False and None
        if self.request.META.get('HTTP_AUTHORIZATION'):
            token_header = self.request.META.get('HTTP_AUTHORIZATION').split(' ')[1]
            try:
                token = Token.objects.get(key=token_header)
            except (KeyError, Token.DoesNotExist):
                return False, None
            return True, token.user
        return False, None

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.get_owner()[0]:
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(),)

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.get_owner()[1])
    #
    #     return super().perform_create(serializer)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            Image.objects.create(owner=self.get_owner()[1],
                                 **serializer.validated_data)
            return Response({'msg': 'image added successfully'},
                            status=status.HTTP_201_CREATED)

        return Response({
            'status': 'Bad request',
            'message': 'Image could not be created with received data.'
            }, status=status.HTTP_400_BAD_REQUEST)
