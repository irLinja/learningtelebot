#!/usr/bin/env python

import telebot
from telebot import types
import ConfigParser

# Reading needed config sections
conf_parse = ConfigParser.RawConfigParser()
conf_parse.read('bot.conf')
_BOT_token = conf_parse.get('bot', 'token')

bot = telebot.TeleBot(_BOT_token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


@bot.chosen_inline_handler(func=lambda chosen_inline_result: True)
def test_chosen(chosen_inline_result):
    pass


@bot.inline_handler(lambda query: query.query == 'text')
def query_text(inline_query):
    try:
        r = types.InlineQueryResultArticle('1', 'Result', 'Result message.')
        r2 = types.InlineQueryResultArticle('2', 'Result2', 'Result message2.')
        bot.answer_inline_query(inline_query.id, [r, r2])
    except Exception as e:
        print(e)

bot.polling()
