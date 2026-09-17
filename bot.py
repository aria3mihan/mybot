import telebot
import os

# update

TOKEN = os.getenv("BOT_TOKEN")

# آیدی عددی کانال‌ها (ثابت داخل کد)
CHANNEL_1 = "-97246777"        # کانال اول: negahemanadar2
CHANNEL_2 = "-1002293940038"   # کانال دوم: seriyalbazi2

bot = telebot.TeleBot(TOKEN)

# تابع بررسی عضویت کاربر در کانال
def is_member(channel, user_id):
    try:
        member = bot.get_chat_member(channel, user_id)
        return member.status in ["member", "administrator", "creator"]
    except Exception:
        return False

# پیام شروع
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(
        message,
        "برای دانلود باید عضو دو کانال باشی:\n\n"
        "کانال اول: https://t.me/negahemanadar2\n"
        "کانال دوم: https://t.me/seriyalbazi2"
    )

# دستور دانلود
@bot.message_handler(commands=['download'])
def download(message):
    user_id = message.from_user.id

    if not is_member(CHANNEL_1, user_id):
        bot.send_message(user_id, f"اول عضو کانال خودم شو:\n{CHANNEL_1}")
        return

    if not is_member(CHANNEL_2, user_id):
        bot.send_message(user_id, f"حالا عضو کانال دوم شو:\n{CHANNEL_2}")
        return

    bot.send_message(user_id, "عضویت تایید شد ❤️ لینک دانلود:\nhttps://example.com/file.mp4")

# اجرای ربات
bot.polling(non_stop=True)
