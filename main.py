from telebot import TeleBot
import ConfigParser

conf_parse = ConfigParser.RawConfigParser()
conf_parse.read('bot.conf')
_BOT_token = conf_parse.get('bot', 'token')

bot = TeleBot(__name__)

@bot.route('/command ?(.*)')
def example_command(message, cmd):
    chat_dest = message['chat']['id']
    msg = u"Command Recieved: {}".format(cmd)

    bot.send_message(chat_dest, msg)


@bot.route('(?!/).+')
def parrot(message):
    chat_dest = message['chat']['id']
    user_msg = message['text']

    msg = u"Did you say {}?".format(user_msg)
    bot.send_message(chat_dest, msg)


if __name__ == '__main__':
    bot.config['api_key'] = _BOT_token
    bot.poll(debug=True)
    #bot.polling(none_stop=True)
