from django_filters import rest_framework as filters
from book.models import Book, Comment


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class BookFilter(filters.FilterSet):
    genre = CharFilterInFilter(field_name='genres__id', lookup_expr='in')
    author = CharFilterInFilter(field_name='authors__id', lookup_expr='in')
    year = filters.RangeFilter()

    class Meta:
        model = Book
        fields = ['genres', 'authors', 'year']


class CommentFilter(filters.FilterSet):
    book = CharFilterInFilter(field_name='book__id', lookup_expr='in')
    user = CharFilterInFilter(field_name='user__id', lookup_expr='in')

    class Meta:
        model = Comment
        fields = ['book', 'user']


