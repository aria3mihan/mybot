import telebot

BOT_TOKEN = "7437089012:AAH3q0eJ2m5z8Yb8v6t8u5rYfR0lF8p0Fqk"
CHANNEL_1 = -10097246777        # negahemanadar2
CHANNEL_2 = -1002455669969      # seriyalbazi2

bot = telebot.TeleBot(BOT_TOKEN)

def is_member(user_id):
    try:
        m1 = bot.get_chat_member(CHANNEL_1, user_id)
        m2 = bot.get_chat_member(CHANNEL_2, user_id)
        return (m1.status in ["member", "administrator", "creator"]) and \
               (m2.status in ["member", "administrator", "creator"])
    except:
        return False

def download_button(episode):
    markup = telebot.types.InlineKeyboardMarkup()
    btn = telebot.types.InlineKeyboardButton(
        text="برای دانلود کلیک کن",
        callback_data=f"download_{episode}"
    )
    markup.add(btn)
    return markup

@bot.message_handler(func=lambda m: m.text.startswith("دانلود قسمت"))
def handle_download_request(message):
    user_id = message.chat.id
    episode = message.text.replace("دانلود قسمت ", "").strip()

    # این پیام، هم دکمهٔ شیشه‌ای می‌سازه، هم نقطهٔ شروع کاربره
    bot.send_message(
        user_id,
        f"برای دانلود قسمت {episode} روی دکمه زیر کلیک کن 👇",
        reply_markup=download_button(episode)
    )

@bot.callback_query_handler(func=lambda call: call.data.startswith("download_"))
def callback_download(call):
    user_id = call.message.chat.id
    episode = call.data.replace("download_", "")

    if not is_member(user_id):
        bot.send_message(
            user_id,
            "برای دانلود باید عضو هر دو کانال باشی ❤️\n\n"
            "کانال اول:\nhttps://t.me/negahemanadar2\n"
            "کانال دوم:\nhttps://t.me/seriyalbazi2\n\n"
            "بعد از عضویت دوباره روی دکمهٔ دانلود بزن 🌿"
        )
        return

    download_link = f"https://t.me/negahemanadar2/{episode}"

    bot.send_message(
        user_id,
        f"عضویت تایید شد ❤️\n\n"
        f"لینک دانلود قسمت {episode}:\n{download_link}"
    )

bot.infinity_polling()
