from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from book.views import (
    BookView,
    CommentCreateView,
    BookFileUploadView,
    CommentApiView,
    CommentEditView,
    CommentDeleteView,
    BookDownloadView,
    BookDetailView, GenreView, AuthorView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/books/', BookView.as_view()),
    path('api/v1/genres/', GenreView.as_view()),
    path('api/v1/authors/', AuthorView.as_view()),
    path('api/v1/book/<int:pk>', BookDetailView.as_view()),
    path('api/v1/comments/', CommentApiView.as_view()),
    path('api/v1/comments/create/', CommentCreateView.as_view()),
    path('api/v1/comments/update/<int:pk>', CommentEditView.as_view()),
    path('api/v1/comments/<int:pk>', CommentDeleteView.as_view()),
    path('api/v1/file/upload', BookFileUploadView.as_view()),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
    path('api/download/<int:pk>', BookDownloadView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
