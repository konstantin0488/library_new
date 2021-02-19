from django.db import models
from django.contrib.auth.models import User


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# class User(models.Model):
#     first_name = models.CharField(max_length=255)
#     second_name = models.CharField(max_length=255)
#     password = models.CharField(max_length=255)
#     email = models.EmailField(max_length=255)
#
#     BLOCK = 'unregistered'
#     ACTIVE = 'registered'
#
#     CHOICES = (
#         (BLOCK, 'unregistered'),
#         (ACTIVE, 'registered'),
#     )
#
#     status = models.CharField(max_length=20, choices=CHOICES)
#
#     def __str__(self):
#         return '{first_name}  {second_name}'.format(first_name=self.first_name, second_name=self.second_name)


class Book(models.Model):
    name = models.CharField(max_length=255)
    year = models.CharField(max_length=255)
    description = models.TextField(max_length=2000)
    genres = models.ManyToManyField(Genre)
    authors = models.ManyToManyField(Author)
    created_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to="books", null=True, blank=True)

    def __str__(self):
        return self.name

    @classmethod
    def get_books(cls):
        return Book.objects.all()


class Comment(models.Model):
    body = models.TextField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return 'Комментарий к книге - {bookName} от пользователя - {userName}'.format(
            bookName=self.book,
            userName=self.user,
        )


# class BookFileUpload(models.Model):
#     name = models.CharField(max_length=500)
#     file = models.FileField(blank=False, null=False)
#     book_file = models.OneToOneField(Book, on_delete=models.CASCADE, default=1)
#
#     def __str__(self):
#         return '{name}.pdf'.format(name=self.name)





