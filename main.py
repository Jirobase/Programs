import os

import telebot
from flask import Flask, request

TOKEN = '2013991614:AAHn_VsH19sg20De17NxGwQ523BClMAJmb8'

APP_URL = f"https://svyatoybot.herokuapp.com/{TOKEN}"

bot = telebot.TeleBot(TOKEN)

server = Flask(__name__)


@bot.message_handler(content_types = ['text'])
def bot_message(message):
    if message.chat.type == 'privet':
        if message.text == 'привет':
            bot.send_message('Ку')
        else:
            bot.send_message("пошли пить пиво")

@server.route('/' + TOKEN, methods = ['POST'])
def get_message():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return '!', 200

@server.route('/')
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=APP_URL)
    return '!', 200

@server.route("/")
def index():
    return "<h1>Hello!</h1>"

if __name__== '__main__':
    server.run(host = '0.0.0.0', port = int(os.environ.get('PORT', 5000)))


