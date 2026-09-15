import telebot
import os

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_USERNAME = os.getenv("CHANNEL_USERNAME")  # مثلا @mychannel

bot = telebot.TeleBot(TOKEN)

def is_member(user_id):
    try:
        member = bot.get_chat_member(CHANNEL_USERNAME, user_id)
        return member.status in ["member", "administrator", "creator"]
    except Exception:
        return False

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "سلام 😊 برای دانلود باید عضو کانال باشی.")

@bot.message_handler(commands=['download'])
def download_file(message):
    user_id = message.from_user.id

    if not is_member(user_id):
        bot.send_message(
            user_id,
            f"برای دانلود باید عضو کانال بشی:\n{CHANNEL_USERNAME}\nبعد از عضویت دوباره /download رو بزن."
        )
        return

    bot.send_message(user_id, "عضوی! الان می‌تونی دانلود کنی 😊")
    # اینجا فایل واقعی رو می‌فرستی
    # bot.send_document(user_id, open("file.mp4", "rb"))

bot.infinity_polling()
