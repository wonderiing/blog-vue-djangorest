from rest_framework import serializers

from blog.models import Post, Notes

class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        exclude = ('is_archived',)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = instance.user.nickname
        if instance.image:
            representation['image'] = instance.image.url
        else:
            representation['image'] = None
        return representation
    
class UserPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('user', 'short_desc', 'title')

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'user': instance.user.nickname,
            'short_desc': instance.short_desc,
            'title': instance.title
        }
    

class NotesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Notes
        fields = '__all__'

    
    def to_representation(self, instance):
        representation =  super().to_representation(instance)
        representation['user'] = instance.user.nickname

        if instance.image:
            representation['image'] = instance.image.url
        else:
            representation['image'] = None
        return representation
 