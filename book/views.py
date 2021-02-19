
from rest_framework import status, generics
from rest_framework.parsers import MultiPartParser, FormParser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from book.filters import BookFilter, CommentFilter
from book.models import Book, Comment, Genre, Author
from book.permissions import IsOwnerOrReadOnly

from book.serializers import (
    BookSerializer,
    CommentCreateSerializer,
    BookFileUploadSerializer,
    CommentDeleteSerializer,
    CommentEditSerializer, CommentSerializer,
    BookDownLoadSerializer,
    BookDetailSerializer, GenreSerializer, AuthorSerializer,
)


class BookView(generics.ListAPIView):

    serializer_class = BookSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = BookFilter
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Book.objects.all()


class BookDetailView(generics.RetrieveAPIView):

    serializer_class = BookDetailSerializer
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()


class CommentApiView(generics.ListAPIView):

    serializer_class = CommentSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CommentFilter
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()


class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentDeleteView(generics.DestroyAPIView):
    serializer_class = CommentDeleteSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    queryset = Comment.objects.all()


class CommentEditView(generics.UpdateAPIView):
    serializer_class = CommentEditSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Comment.objects.all()


class BookFileUploadView(generics.CreateAPIView):

    parser_classes = (MultiPartParser, FormParser)
    serializer_class = BookFileUploadSerializer
    permission_classes = [IsAdminUser]


class BookDownloadView(generics.RetrieveAPIView):
    serializer_class = BookDownLoadSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        book = Book.objects.all()
        return book


class GenreView(generics.ListAPIView):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()


class AuthorView(generics.ListAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()





