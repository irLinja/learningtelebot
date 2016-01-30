import telebot
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


'''
@bot.message_handler(commands=['start'])
def send_welcome(message):
    msg = u"Welcome this is telebot (:"

    bot.send_message(message, message.text)


@bot.message_handler(func=lambda message: True)
def echo(message):
    user_msg = message['text']

    msg = u"Did you say {}?".format(user_msg)
    bot.reply_to(message, message.text)
'''

bot.polling()

