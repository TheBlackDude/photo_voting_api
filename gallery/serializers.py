from rest_framework import serializers
from account.serializers import AccountSerializer
from .models import Image, Vote


class ImageInfoSerializer(serializers.ModelSerializer):
    owner = AccountSerializer(read_only=True, required=False)

    class Meta:
        model = Image
        fields = ('id', 'owner', 'image', 'title', 'description', 'category',
                  'location', 'created_at')
        read_only_fields = ('id', 'created_at', 'image')

    def get_validation_exclusions(self, *args, **kwargs):
        exclusions = super().get_validation_exclusions(*args, **kwargs)

        return exclusions + ['owner']


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ('id', 'image')


class VoteSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(read_only=True, required=False)

    class Meta:
        model = Vote
        fields = ('id', 'image', 'upvote', 'downvote')
        read_only_fields = ('id',)
