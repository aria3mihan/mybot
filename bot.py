
import telebot
import os
# update
TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_1 = os.getenv("CHANNEL_1")   # کانال خودت
CHANNEL_2 = os.getenv("CHANNEL_2")   # کانال دوم

bot = telebot.TeleBot(TOKEN)

def is_member(channel, user_id):
    try:
        member = bot.get_chat_member(channel, user_id)
        return member.status in ["member", "administrator", "creator"]
    except Exception:
        return False

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(
        message,
        "برای دانلود باید عضو هر دو کانال باشی:\n\n"
        "کانال اول: https://t.me/negahemanadar2"
        "کانال دوم: https://t.me/seriyalbazi2"
    )

@bot.message_handler(commands=['download'])
def download(message):
    user_id = message.from_user.id

    if not is_member(CHANNEL_1, user_id):
        bot.send_message(user_id, f"اول عضو کانال خودم شو:\n{CHANNEL_1}")
        return

    if not is_member(CHANNEL_2, user_id):
        bot.send_message(user_id, f"حالا عضو کانال دوم شو:\n{CHANNEL_2}")
        return

    bot.send_message(user_id, "عضویت تایید شد ❤️\nاینم لینک دانلودت:\nhttps://example.com/file.mp4")
bot.polling(none_stop=True)
