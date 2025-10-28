# app.py: Telegram bot kodi
# Bu versiya Telegram Web App (TWA) ni ochish uchun tugma qo'shadi.

import logging
import threading
import time 

from telegram import Update, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes
from telegram.constants import ParseMode
from telegram import InlineKeyboardButton, InlineKeyboardMarkup # Tugmalar uchun

# app.py: Telegram bot kodi
# Fayl manzili: C:\Users\user\Desktop\SignalBot\app.py

import logging
import threading
import time 

from telegram import Update, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes
from telegram.constants import ParseMode # ParseMode endi ishlatilmaydi
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

# ==============================================================================
# 1. BOT KONFIGURATSIYASI VA WEB APP MANZILI
# ==============================================================================

TOKEN = "8276019572:AAH8guAm9otOtGakG42eej46cb2rdhgyWGw" 

# BotFatherda o'rnatilgan Web App URL.
WEB_APP_URL = "https://kamranchik010-bot.github.io/gamehub/" 

# ==============================================================================
# 2. LOGLARNI SOZLASH
# ==============================================================================
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# ==============================================================================
# 3. BUYRUQLAR (HANDLERS)
# ==============================================================================

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """/start buyrug'iga javob beradi va Web App tugmasini yuboradi."""
    user = update.effective_user
    logger.info(f"Foydalanuvchi Web App tugmasini so'radi: {user.id}")

    # Web App'ni ochish uchun tugma yaratish
    web_app_info = WebAppInfo(url=WEB_APP_URL)
    
    keyboard = [
        [
            InlineKeyboardButton(
                "▶️ O'yin markazini ochish", 
                web_app=web_app_info
            )
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # reply_html ishlatilgani uchun 'parse_mode=...' ni olib tashladik.
    await update.message.reply_html(
        rf"Assalomu Alaykum, {user.mention_html()}! SignalBot ishga tushirildi. O'yin markaziga kirish uchun pastdagi tugmani bosing:",
        reply_markup=reply_markup
    )

# ==============================================================================
# 4. BOTNI ISHGA TUSHIRISH
# ==============================================================================

def start_polling(application: Application):
    """Xatolarni bartaraf etish uchun pollingni alohida jarayonda boshlaydi."""
    try:
        application.run_polling(allowed_updates=Update.ALL_TYPES)
    except Exception as e:
        logger.error(f"Polling xatosi yuz berdi: {e}")

def main() -> None:
    """Botning asosiy ishga tushirish funksiyasi."""
    
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start_command))
    
    bot_thread = threading.Thread(
        target=start_polling, 
        args=(application,), 
        daemon=True 
    )
    bot_thread.start()
    
    print("\n=======================================================")
    print(f"SignalBot ishga tushirildi! Web App URL: {WEB_APP_URL}")
    print("Oynani yopmang, aks holda bot to'xtaydi.")
    print("=======================================================\n")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        logger.info("Bot o'chirildi.")
        pass

if __name__ == "__main__":
    main()
