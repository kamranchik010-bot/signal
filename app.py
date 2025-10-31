import telebot
from telebot.types import WebAppInfo, KeyboardButton, ReplyKeyboardMarkup

# --- Konfiguratsiya ---
# Telegram bot tokeningiz
TOKEN = "8215882181:AAGT57dC8PGxlTOjYsZOABysBzMvksKw2yQ"

# GitHub Pages'ga joylashtirilgan Web App (index.html) ning URL manzili
# MUHIM: Bu manzilni o'zingizning GitHub Pages manzilingiz bilan tasdiqlang
WEB_APP_URL = "https://kamranchik010-bot.github.io/signalxbet/index.html" 

# Botni ishga tushirish
bot = telebot.TeleBot(TOKEN)

# --- Tugmalar va interfeys ---
def get_main_keyboard():
    # Telegram Web App uchun ma'lumot
    web_app_info = WebAppInfo(url=WEB_APP_URL)
    
    # "Signal Markazini Ochish" tugmasini yaratish
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    
    # Tugmaga matn berish va unga Web App ma'lumotini ulash
    btn = KeyboardButton(text="🚀 Signal Markazini Ochish", web_app=web_app_info)
    
    keyboard.add(btn)
    return keyboard

# --- Bot mantiqi ---
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    """/start va /help buyruqlariga javob beruvchi funksiya."""
    try:
        # Foydalanuvchiga xabar yuborish
        bot.send_message(
            chat_id=message.chat.id,
            text=f"Assalomu alaykum, {message.from_user.first_name}!\n\nSignal Markaziga xush kelibsiz. Botni ishga tushirish uchun quyidagi tugmani bosing:",
            reply_markup=get_main_keyboard()
        )
        print(f"Foydalanuvchiga yuborildi: {message.from_user.id}")
        
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")

# --- Asosiy ishga tushirish bloki ---
if __name__ == '__main__':
    print("=======================================================")
    print(f"✅ Telegram Bot ishga tushirildi!")
    print(f"🌐 Web App URL: {WEB_APP_URL}")
    print("Oynani yopmang, aks holda bot to'xtaydi. To'xtatish uchun CTRL+C bosing.")
    print("=======================================================")
    try:
        # Botni doimiy ravishda so'rovlar qabul qilish uchun ishga tushirish
        bot.polling(none_stop=True, interval=0)
    except Exception as e:
        print(f"Kritik xato: Bot to'xtadi. {e}")