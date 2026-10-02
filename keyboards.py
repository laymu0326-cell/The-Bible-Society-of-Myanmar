# keyboards.py
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

# Level 1: Main Menu
def get_main_menu_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(" အကြောင်းအရာ", callback_data='btn_about'),
            InlineKeyboardButton(" ဆက်သွယ်ရန်", callback_data='btn_contact'),
        ],
        [
            # https:// ထည့်သွင်း ပြင်ဆင်ထားပါသည်
            InlineKeyboardButton(" Website သို့သွားရန်", url='https://bsmyanmar.org')
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

# Level 2: About Menu အောက်မှ Sub-Menu
def get_about_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("လိပ်စာ ", callback_data='sub_address'),
            InlineKeyboardButton(" ဆိုင်ဖွင့်ချိန်", callback_data='sub_time'),
            InlineKeyboardButton(" ရုံးပိတ်ရက်", callback_data='sub_holiday'),
        ],
        [
            InlineKeyboardButton(" မူလ Menu သို့ပြန်သွားရန်", callback_data='btn_back_main')
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

# Level 3: About Detail အောက်မှ Back Button
def get_back_to_about_keyboard():
    keyboard = [
        [InlineKeyboardButton(" အကြောင်းအရာ Menu သို့ပြန်သွားရန်", callback_data='btn_back_about')]
    ]
    return InlineKeyboardMarkup(keyboard)

# Level 2: Contact Menu အောက်မှ Sub-Menu
def get_contact_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(" မှာယူရန်နှင့်ဆက်သွယ်ရန်", callback_data='sub_phone'),
            InlineKeyboardButton(" Facebookpage", callback_data='sub_page'),
            InlineKeyboardButton(" TikTok Link", callback_data='sub_tiktok'),
        ],
        [
            InlineKeyboardButton(" မူလ Menu သို့ပြန်သွားရန်", callback_data='btn_back_main')
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

# Level 3: Contact Detail အောက်မှ Back Button
def get_back_to_contact_keyboard():
    keyboard = [
        [InlineKeyboardButton(" ဆက်သွယ်ရန် Menu သို့ပြန်သွားရန်", callback_data='btn_back_contact')]
    ]
    return InlineKeyboardMarkup(keyboard)

# General Back Button Keyboard
def get_back_keyboard():
    keyboard = [
        [InlineKeyboardButton(" နောက်သို့", callback_data='btn_back')]
    ]
    return InlineKeyboardMarkup(keyboard)