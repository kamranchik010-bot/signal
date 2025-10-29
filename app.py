# app.py: Telegram bot kodi
# Fayl manzili: C:\Users\user\Desktop\SignalBot\app.py

import logging
import threading
import time

from telegram import Update, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

# ==============================================================================
# 1. BOT KONFIGURATSIYASI VA WEB APP MANZILI
# ==============================================================================

TOKEN = "8276019572:AAH8guAm9otOtGakG42eej46cb2rdhgyWGw"

# Web App manzili (GitHub Pages)
# KESHNI TOZALASH UCHUN: Oxiriga "?v=2" qo'shildi. Bu manzilni har safar
# o'zgartirsangiz (masalan, ?v=3), kesh majburan yangilanadi.
WEB_APP_URL = "https://kamranchik010-bot.github.io/gamehub/index.html?v=2"

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
    # XATO TUZATILDI: Endi to'g'ri WebAppInfo(url=WEB_APP_URL) ishlatildi
    web_app_info = WebAppInfo(url=WEB_APP_URL)

    keyboard = [
        [
            InlineKeyboardButton(
                "📈 Signal Markazini Ochish",
                web_app=web_app_info
            )
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # HTML xabar yuborish
    await update.message.reply_html(
        rf"Assalomu Alaykum, {user.mention_html()}! SignalBot ishga tushirildi. Signal markaziga kirish uchun pastdagi tugmani bosing:",
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
    # XATO TUZATILDI: Print funksiyasida WEB_APP_URL o'zgaruvchisi ishlatildi
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
