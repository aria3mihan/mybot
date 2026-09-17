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

# هر پیام که کاربر بده، این اجرا می‌شود
@bot.message_handler(func=lambda message: True)
def check_membership(message):
    user_id = message.from_user.id

    # چک کانال اول
    if not is_member(CHANNEL_1, user_id):
        bot.send_message(
            user_id,
            "برای دانلود باید عضو کانال اول باشی:\n"
            "https://t.me/negahemanadar2"
        )
        return

    # چک کانال دوم
    if not is_member(CHANNEL_2, user_id):
        bot.send_message(
            user_id,
            "برای دانلود باید عضو کانال دوم باشی:\n"
            "https://t.me/seriyalbazi2"
        )
        return

    # اگر عضو هر دو کانال بود
    bot.send_message(
        user_id,
        "عضویت تایید شد ❤️\n"
        "لینک دانلود:\nhttps://example.com/file.mp4"
    )

# اجرای ربات
bot.polling(non_stop=True)
