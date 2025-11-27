import telebot
import os
from telebot import types
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Bot ishga tushdi!")

bot.infinity_polling()
