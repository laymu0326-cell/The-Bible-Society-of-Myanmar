# handlers.py
from telegram import Update
from telegram.ext import ContextTypes
from keyboards import (
    get_main_menu_keyboard,
    get_about_keyboard,
    get_contact_keyboard,
    get_back_to_about_keyboard,
    get_back_to_contact_keyboard
)

# /start Command Handler
async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 မင်္ဂလာပါ! အောက်ပါ မီနူးမှ ရွေးချယ်နိုင်ပါတယ် -",
        reply_markup=get_main_menu_keyboard()
    )

# Button နှိပ်လိုက်မှုများကို စိစစ်သည့် Callback Query Handler
async def callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    # --- Main Menu သို့ ပြန်သွားခြင်း ---
    if data in ['btn_back_main', 'btn_main']:
        await query.edit_message_text(
            "👋 မင်္ဂလာပါ! BSmyanmarbot မှကြိုဆိုပါသည်။\nအောက်ပါ မီနူးမှ ရွေးချယ်နိုင်ပါတယ် -",
            reply_markup=get_main_menu_keyboard()
        )

    # --- About Section ---
    elif data in ['btn_about', 'btn_back_about']:
        await query.edit_message_text(
            "ℹ️ **အကြောင်းအရာ Menu**\n\nများကို ရွေးချယ်ပါ -",
            reply_markup=get_about_keyboard(),
            parse_mode="Markdown"
        )
    elif data == 'sub_address':
        await query.edit_message_text(
            "📍 **လိပ်စာ**\n\nအမှတ်(၂၆၂)၊ ဆူးလေဘုရားလမ်း၊\n ကျောက်တံတားမြို့နယ်၊ ရန်ကုန်မြို့၊။",
            reply_markup=get_back_to_about_keyboard(),
            parse_mode="Markdown"
        )
    elif data == 'sub_time':
        await query.edit_message_text(
            "⏰ **ဆိုင်ဖွင့်ချိန်**\n\nမနက် ၉:၀၀ မှ ညနေ ၄:၀၀ ထိ",
            reply_markup=get_back_to_about_keyboard(),
            parse_mode="Markdown"
        )
    elif data == 'sub_holiday':
        await query.edit_message_text(
            "📅 **ရုံးပိတ်ရက်**\n\nစနေ၊ တနင်္ဂနွေနှင့် အစိုးရရုံးပိတ်ရက်အတိုင်း ပိတ်ပါသည်။",
            reply_markup=get_back_to_about_keyboard(),
            parse_mode="Markdown"
        )

    # --- Contact Section ---
    elif data in ['btn_contact', 'btn_back_contact']:
        await query.edit_message_text(
            "📞 **ဆက်သွယ်ရန် Menu**\n\nအောက်ပါလမ်းကြောင်းများမှ ဆက်သွယ်နိုင်ပါတယ် -",
            reply_markup=get_contact_keyboard(),
            parse_mode="Markdown"
        )
    elif data == 'sub_phone':
        await query.edit_message_text(
            "📞 **မှာယူရန်နှင့် ဆက်သွယ်ရန်**\n\n09976405188\n0943073538\n09252856606\n သို့ ဆက်သွယ်နိုင်ပါသည်။",
            reply_markup=get_back_to_contact_keyboard(),
            parse_mode="Markdown"
        )
    elif data == 'sub_page':
        await query.edit_message_text(
            "📘 **Facebook Page**\n\nhttps://www.facebook.com/share/1EaKZQf1mh/",
            reply_markup=get_back_to_contact_keyboard()
        )
    elif data == 'sub_tiktok':
        await query.edit_message_text(
            "🎵 **TikTok Link**\n\nhttps://www.tiktok.com/@the.bible.society1?_r=1&_t=ZS-9ABtnzk9d37",
            reply_markup=get_back_to_contact_keyboard()
        )