from rest_framework.serializers import ModelSerializer
from book.models import (
    Book,
    Comment, Genre, Author,
)


class BookSerializer(ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'name', 'year')


class BookDetailSerializer(ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'


class CommentSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'


class CommentCreateSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = ('body', 'book',)


class CommentDeleteSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class CommentEditSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class BookFileUploadSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookDownLoadSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ['file']


class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

