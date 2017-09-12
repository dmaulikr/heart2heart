from .models import Chat, ChatLine
from rest_framework import serializers
from heartuser.serializers import HeartUserSerializer

class ChatSerializer(serializers.ModelSerializer):
    users = HeartUserSerializer(many=True)
    class Meta:
        model = Chat
        fields = '__all__'
    
    def create(self, validated_data):
        pass
    
    def update(self, instance, validated_data):
        pass

class ChatLineSerializer(serializers.ModelSerializer):
    chat_id = ChatSerializer()
    user = HeartUserSerializer()
    message = serializers.CharField()
    created_at = serializers.DateTimeField()

    class Meta:
        model = ChatLine
        fields = '__all__'

    def create(self, validated_data):
        pass
    
    def update(self, instance, validated_data):
        pass