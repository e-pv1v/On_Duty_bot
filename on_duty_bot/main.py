import os
import telebot
from dotenv import load_dotenv

load_dotenv()  # load env variables from .env file

# WhoIsOnDuty_bot
bot = telebot.TeleBot(os.getenv("TOKEN"))  # Token from BotFather


@bot.message_handler(commands=["start"])  # Bot Greeting
def get_started(msg):
    """
    Creates greeting message for users
    """
    mess = f"Привет, <b>{msg.from_user.first_name} <u>{''if not msg.from_user.last_name else msg.from_user.last_name }</u></b>.👋\nЯ бот, который помогает узнать кто на смене. 🫡\nЧтобы узнать что я умею нажмите /help 🤔"
    bot.send_message(msg.chat.id, mess, parse_mode="html")


# Run Bot
bot.polling(none_stop=True)
