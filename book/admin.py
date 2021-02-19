from django.contrib import admin

from book.models import (
    Book,
    # User,
    Comment,
    Genre,
    Author,
    # BookFileUpload
)


# admin.site.register(User)
admin.site.register(Genre)
admin.site.register(Author)
# admin.site.register(BookFileUpload)


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_genres', 'get_authors')

    def get_genres(self, obj):
        return obj.genres.get()
    get_genres.short_description = 'Genres'

    def get_authors(self, obj):
        return obj.authors.get()
    get_authors.short_description = 'Authors'


admin.site.register(Book, BookAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'body', 'created_at')


admin.site.register(Comment, CommentAdmin)