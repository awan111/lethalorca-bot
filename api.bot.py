import os
from flask import Flask, request
import telebot

TOKEN = '8689687590:AAHSzJ_36tERZZzo4LhSMIavF30lUZI18wE'
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return "OK", 200
    return "Forbidden", 403

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_text = (
        "🤖 LethalOrca ($LORCA) Bot Active on Vercel!\n\n"
        "Available commands:\n"
        "/price - Check live price & market cap\n"
        "/contract - Get official token contract\n"
        "/socials - Official links"
    )
    bot.reply_to(message, welcome_text)

@bot.message_handler(commands=['price'])
def price_command(message):
    bot.reply_to(message, "Tracking live price via Helius & Vercel...")

@app.route('/')
def index():
    return "LethalOrca Bot Server is live!", 200
