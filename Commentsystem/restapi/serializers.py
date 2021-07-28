from rest_framework import serializers
from .models import Page, Comment, Subcomment

class SubcommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcomment
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    subcomment = SubcommentSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = "__all__"

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page 
        fields = "__all__"
