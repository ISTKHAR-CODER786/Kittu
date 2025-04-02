from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

import config
from NEXIOMUSIC import app

class BUTTONS(object):
    MBUTTON = [
        [
            InlineKeyboardButton("𝐈꯭꯭ѕ꯭꯭፝֠֩‌тк꯭꯭н፝֠֩‌α꯭꯭я꯭꯭", url="https://t.me/ll_ISTKHAR_BABY_lll")
        ],
        [
            InlineKeyboardButton("⌯ ʙᴧᴄᴋ ᴛσ ʜσϻє ⌯", callback_data="settingsback_helper"),
            
        ]
        ]
    
    SBUTTON = [
 
        [
            InlineKeyboardButton("𝐈꯭꯭ѕ꯭꯭፝֠֩‌тк꯭꯭н፝֠֩‌α꯭꯭я꯭꯭", url="https://t.me/THUNDERDEVS"),
        ],
        [
            InlineKeyboardButton("ᴛєᴄʜ", url="https://t.me/THUNDERDEVS"),
        ],
        [
            InlineKeyboardButton("ᴄʜᴧᴛ ɢᴄ", url="https://t.me/+pnDJxCG5VVphMTVl"),
            InlineKeyboardButton("⎯꯭‌🫧᪵᪳ ⃪꯭꯭🇨꯭꯭𝗥꯭𝗔꯭𝗭꯭𝗬 ꯭🇼꯭꯭❍꯭𝗥꯭𝗟꯭𝗗꯭🌸⃪꯭𝆭⎯꯭𝆭⎯ ꯭", url="https://t.me/+pnDJxCG5VVphMTV"),
        ],
        [
            InlineKeyboardButton("⌯ ʙᴧᴄᴋ ᴛσ ʜσϻє ⌯", callback_data="settingsback_helper"),
            
        ]
        ]
    
    ABUTTON = [
        [
            InlineKeyboardButton("ᴧʙσυᴛ", url="https://t.me/THUNDERDEVS"),
            InlineKeyboardButton("ʜєʟᴘ | ɪηғσ", callback_data="settings_back_helper"),
        ],
        [
            InlineKeyboardButton("ʙᴧsɪᴄ ɢυɪᴅє", callback_data="ABOUT_BACK HELP_GUIDE"),
            InlineKeyboardButton("ᴅσηᴧᴛє", callback_data="ABOUT_BACK HELP_DONATE"),
        ],
        [
            InlineKeyboardButton("⌯ ʙᴧᴄᴋ ᴛσ ʜσϻє ⌯", callback_data="settingsback_helper"),
            
        ]
        ]
