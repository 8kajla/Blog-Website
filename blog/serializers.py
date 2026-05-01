from rest_framework import serializers
from .models import Post
from .models import Author

class AuthorSerializerPost(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields = ['first_name','last_name']



class PostSerializer(serializers.ModelSerializer):
    author= AuthorSerializerPost(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'