from django.http import Http404
from rest_framework import permissions, viewsets, status, views
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from .models import Image
from .serializers import ImageInfoSerializer, ImageSerializer, VoteSerializer


class ImageViewSet(viewsets.ModelViewSet):
    """
    API endpoint for creating and listing Images
    """
    queryset = Image.objects.order_by('-created_at')
    serializer_class = ImageInfoSerializer

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
            return Response({'msg': 'image info added successfully',
                             'id': Image.objects.last().id},
                            status=status.HTTP_201_CREATED)

        return Response({
                        'status': 'Bad request',
                        'message': 'Image info could not be created with received data.'},
                        status=status.HTTP_400_BAD_REQUEST)


class ImageApiView(APIView):
    """
    Api endpoint for uploading image
    """
    def get_object(self, pk):
        try:
            return Image.objects.get(pk=pk)
        except Image.DoesNotExist:
            raise Http404

    def put(self, request, pk):
        image = self.get_object(pk)
        serializer = ImageSerializer(
            image, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


class VoteApiView(APIView):
    """
    Api endpoint for voting on images
    """
    def get_object(self, pk):
        try:
            return Image.objects.get(pk=pk)
        except Image.DoesNotExist:
            raise Http404

    def put(self, request, pk):
        image = self.get_object(pk)
        serializer = VoteSerializer(
            image, data=request.data)
        if serializer.is_valid():
            new_upvote = serializer.validated_data.get('upvote')
            new_downvote = serializer.validated_data.get('downvote')
            upvote = image.upvote + new_upvote
            downvote = image.downvote + new_downvote
            serializer.save(
                upvote=upvote, downvote=downvote
            )
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
