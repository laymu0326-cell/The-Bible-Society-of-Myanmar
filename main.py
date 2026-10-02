import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CallbackQueryHandler, CommandHandler,MessageHandler, filters

# တခြား ဖိုင်များမှ Handlers များကို Import လုပ်ခြင်း
from handlers import  callback_handler, start_handler

# .env ဖိုင်မှ Token ကို ဖတ်ယူခြင်း
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

def main():
    if not BOT_TOKEN:
        print("Error: BOT_TOKEN ကို .env ဖိုင်တွင် ထည့်သွင်းပေးပါ။")
        return

    # Bot တည်ဆောက်ခြင်း
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Handlers များ ချိတ်ဆက်ခြင်း
    app.add_handler(CommandHandler("start", start_handler))
    app.add_handler(CommandHandler("menu", start_handler))
    app.add_handler(CallbackQueryHandler(callback_handler))

    print("Bot စတင်ပွင့်နေပါပြီ...")
    app.run_polling()

if __name__ == '__main__':
    main()