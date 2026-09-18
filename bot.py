
import telebot
from telebot import types
import os

# گرفتن توکن از متغیرهای Railway
BOT_TOKEN = os.getenv("BOT_TOKEN")

CHANNEL_1 = -10097246777        # negahemanadar2
CHANNEL_2 = -1002455669969      # seriyalbazi2

bot = telebot.TeleBot(BOT_TOKEN)

# چک کردن عضویت کاربر در هر دو کانال
def is_member(user_id):
    try:
        m1 = bot.get_chat_member(CHANNEL_1, user_id)
        m2 = bot.get_chat_member(CHANNEL_2, user_id)
        return (m1.status in ["member", "administrator", "creator"]) and \
               (m2.status in ["member", "administrator", "creator"])
    except:
        return False

# هندلر شروع
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id

    if not is_member(user_id):
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("عضویت در کانال ۱", url="https://t.me/negahemanadar2")
        btn2 = types.InlineKeyboardButton("عضویت در کانال ۲", url="https://t.me/seriyalbazi2")
        btn3 = types.InlineKeyboardButton("عضویت را چک کن ✔️", callback_data="check")
        markup.add(btn1)
        markup.add(btn2)
        markup.add(btn3)

        bot.reply_to(message, "برای دانلود باید عضو هر دو کانال باشی ❤️", reply_markup=markup)
        return

    bot.reply_to(message, "سلام عزیزم 😍\nشماره قسمت رو بفرست تا لینک دانلود رو بدم.")

# چک کردن عضویت با دکمهٔ شیشه‌ای
@bot.callback_query_handler(func=lambda call: call.data == "check")
def check_membership(call):
    user_id = call.from_user.id

    if is_member(user_id):
        bot.answer_callback_query(call.id, "عضویت تأیید شد ✔️")
        bot.send_message(user_id, "عالیه 😍\nحالا شماره قسمت رو بفرست.")
    else:
        bot.answer_callback_query(call.id, "هنوز عضو نیستی ❌")
        bot.send_message(user_id, "برای دانلود باید عضو هر دو کانال باشی ❤️")

# هندلر دانلود قسمت‌ها
@bot.message_handler(func=lambda m: True)
def download_handler(message):
    user_id = message.from_user.id

    if not is_member(user_id):
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("عضویت در کانال ۱", url="https://t.me/negahemanadar2")
        btn2 = types.InlineKeyboardButton("عضویت در کانال ۲", url="https://t.me/seriyalbazi2")
        btn3 = types.InlineKeyboardButton("عضویت را چک کن ✔️", callback_data="check")
        markup.add(btn1)
        markup.add(btn2)
        markup.add(btn3)

        bot.reply_to(message, "برای دانلود باید عضو هر دو کانال باشی ❤️", reply_markup=markup)
        return

    text = message.text.strip()

    if text.startswith("دانلود قسمت"):
        try:
            number = text.replace("دانلود قسمت", "").strip()
            link = f"https://yourserver.com/download/{number}.mp4"
            bot.reply_to(message, f"لینک دانلود قسمت {number} 👇\n{link}")
        except:
            bot.reply_to(message, "شماره قسمت نامعتبره عزیزم ❌")
    else:
        bot.reply_to(message, "شماره قسمت رو اینجوری بفرست:\n\nدانلود قسمت ۵۸")

# اجرای ربات
bot.polling(none_stop=True)
