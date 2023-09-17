# in & as LazyDeveloper
# Please Don't Remove Credit

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "MdiskSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -100))
    BOT_USERNAME = os.environ.get("BOT_USERNAME")
    BOT_OWNER = int(os.environ.get("BOT_OWNER"))
    DATABASE_URL = os.environ.get("DATABASE_URL")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    ABOUT_BOT_TEXT = """<b> <a href='https://t.me/movies_villa_backup'>Mᴏᴠɪᴇs Vɪʟʟᴀ</a> ɪs ᴀɴ ᴏᴘᴇɴ sᴏᴜʀᴄᴇ ᴘʀᴏJᴇᴄᴛ.

    Devs: 
        <a href='https://t.me/movies_villa_backup'>❤️👑ᴿᴼᵞᴬᴸ ᴼˢᴹ ᴹᴱᴴᴿᴬ👑❤️p</a>
    
    
🤖 Mʏ Nᴀᴍᴇ: <a href='https://t.me/Movies_villae'>Mᴏᴠɪᴇs Vɪʟʟᴀ Sᴇᴀʀᴄʜ Bᴏᴛ</a>

📝 Lᴀɴɢᴜᴀɢᴇ: <a href='https://www.python.org'>Python V3</a>

📚 Lɪʙʀᴀʀʏ: <a href='https://docs.pyrogram.org'>Pyrogram</a>

📡 Sᴇʀᴠᴇʀ: <a href='https://heroku.com'>Heroku</a>

📡 Sᴇʀᴠᴇʀ 2: <a href='https://heroku.com'>koyeb</a> <i>comming soon</i>

👨‍💻 Dᴇᴠᴇʟᴏᴘᴇʀ Cʜᴀɴɴᴇʟ: <a href='https://t.me/movies_villa_backup'>Mᴏᴠɪᴇs Vɪʟʟᴀ</a></b>
"""

    ABOUT_HELP_TEXT = """<b>👑Dᴇᴠᴇʟᴏᴘᴇʀ👑  : <a href='https://t.me/ROYAL_GAGAN_DEEP_SINGH_MEHRA'>👑Dᴇᴠᴇʟᴏᴘᴇʀ👑</a>

Iғ Yᴏᴜ Wᴀɴᴛ Yᴏᴜʀ Oᴡɴ Bᴏᴛ Lɪᴋᴇ Tʜɪs Tʜᴇɴ Yᴏᴜ Cᴀɴ Cᴏɴᴛᴀᴄᴛ Oᴜʀ Dᴇᴠᴇʟᴏᴘᴇʀ.</b>
"""

    HOME_TEXT = """
<b>Hᴇʟʟᴏ ! {}😅,

 I'ᴍ ᴛʜᴇ ᴏɴᴇ ᴀɴᴅ ᴏɴʟʏ ғᴀsᴛᴇsᴛ URL ғɪɴᴅᴇʀ BOT. Aᴅᴅ ᴍᴇ ᴛᴏ ᴀɴʏ Gʀᴏᴜᴘ ᴀɴᴅ Gɪᴠᴇ ᴍᴇ Hᴜɴᴛɪɴɢ ʀɪɢʜᴛs!!

I ᴡɪʟʟ ʙᴇ ᴏɴʟʏ ʏᴏᴜʀs ɪғ ʏᴏᴜ ᴡɪʟʟ ʀᴇsᴛʀɪᴄᴛ ᴀᴅᴅɪɴɢ ᴍᴇ ᴛᴏ ᴏᴛʜᴇʀ ɢʀᴏᴜᴘs.
Go to @BotFather to change settings.

Dᴏɴ'ᴛ ʙᴇ sᴀᴅ ! Yᴏᴜʀ ᴀʟʟ ᴜʀʟs ᴀʀᴇ ɪɴ sᴀғᴇ Hᴀɴᴅ.

»»» <b>❤️👑ᴿᴼᵞᴬᴸ ᴼˢᴹ ᴹᴱᴴᴿᴬ👑❤️</b> «««

🔺Thank You <a href='https://t.me/movies_villa_backup'>❤️👑ᴿᴼᵞᴬᴸ ᴼˢᴹ ᴹᴱᴴᴿᴬ👑❤️</a>🔺 </b>
"""


    START_MSG = """
<b>Hᴇʟʟᴏ ! {}😅,

I'ᴍ ᴛʜᴇ ᴏɴᴇ ᴀɴᴅ ᴏɴʟʏ ғᴀsᴛᴇsᴛ URL & ᴘᴏsᴛ ғɪɴᴅᴇʀ BOT. Aᴅᴅ ᴍᴇ ᴛᴏ ᴀɴʏ Gʀᴏᴜᴘ ᴀɴᴅ Gɪᴠᴇ ᴍᴇ Hᴜɴᴛɪɴɢ ʀɪɢʜᴛs !!
Dᴏɴ'ᴛ ʙᴇ sᴀᴅ ! Yᴏᴜʀ ᴀʟʟ ᴜʀʟs ᴀʀᴇ ɪɴ sᴀғᴇ Hᴀɴᴅ.</b>

   »»»» <b>❤️👑ᴿᴼᵞᴬᴸ ᴼˢᴹ ᴹᴱᴴᴿᴬ👑❤️</b> ««««

💸<b>Dᴏɴᴀᴛᴇ ᴜs ᴛᴏ Kᴇᴇᴘ sᴇʀᴠɪᴄᴇ Aʟɪᴠᴇ.💸</b>
»» A sᴍᴀʟʟ ᴀᴍᴏᴜɴᴛ ᴏғ ₹5 - ₹20 - ₹50 - ₹100 ᴡɪʟʟ ʙᴇ ɢʀᴇᴀᴛ ʜᴇʟᴘ !
🔺 Tʜᴀɴᴋ Yᴏᴜ 🔺 
"""

