from rest_framework import serializers
from chat.models import Message
from users.models import UserAccount


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserAccount
        fields = ['first_name', 'password']


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.SlugRelatedField(many=False, slug_field='first_name', queryset=UserAccount.objects.all())
    receiver = serializers.SlugRelatedField(many=False, slug_field='first_name', queryset=UserAccount.objects.all())

    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'message', 'timestamp']
