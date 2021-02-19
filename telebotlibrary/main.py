import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "library.settings")
import django
django.setup()

import telebot
from telebot import types

from book.models import Book, Genre

bot = telebot.TeleBot('1648368349:AAFDnpykUJes13wN-WsIJ6RwK4VNTchUP3E')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Здравствуйте!')


@bot.message_handler(commands=['show'])
def show_message(message):
    genres = Genre.objects.all()
    markup = types.InlineKeyboardMarkup()
    for genre in genres:
        markup.add(types.InlineKeyboardButton(text=genre.name, callback_data=genre.id))

    bot.send_message(message.chat.id, text="Какой жанр книги вы предпочитаете?", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    bot.answer_callback_query(callback_query_id=call.id, text="Идет поиск книг")
    genre_id = call.data

    answer = Book.objects.filter(genres=genre_id)
    for book in answer:
        bot.send_message(call.message.chat.id, str(book))
        # bot.send_document(call.message.chat.id, book.file)


bot.polling()
