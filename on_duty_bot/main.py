import os
import telebot
from dotenv import load_dotenv
from telebot import types

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


@bot.message_handler(commands=["help"])  # Creating buttons
def get_task_button(msg):
    """
    Creates keyboard for selecting bot task
    """
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    current_shift = types.KeyboardButton("Кто на смене?")
    previous_shift = types.KeyboardButton("Кто был на смене?")
    next_shift = types.KeyboardButton("Кто будет на смене?")
    markup.add(current_shift, previous_shift, next_shift)
    bot.send_message(msg.chat.id, "Выберите что хотите узнать", reply_markup=markup)


@bot.message_handler()  # Any user message handler
def get_user_text(msg):
    """
    Handles user messages
    """
    if msg.text == "Кто на смене?":
        bot.send_message(msg.chat.id, "get_current_shift()", parse_mode="html")
    elif msg.text == "Кто был на смене?":
        bot.send_message(msg.chat.id, "get_previous_shift()", parse_mode="html")
    elif msg.text == "Кто будет на смене?":
        bot.send_message(msg.chat.id, "get_next_shift()", parse_mode="html")
    else:
        bot.send_message(
            msg.chat.id, "На данный момент не готов ответить 😅", parse_mode="html"
        )


# Run Bot
bot.polling(none_stop=True)
