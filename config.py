#(©)Anime_Eternals




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", ""))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6497757690"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluser0")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL_1 = int(os.environ.get("FORCE_SUB_CHANNEL_1", "-1001473043276"))
FORCE_SUB_CHANNEL_2 = int(os.environ.get("FORCE_SUB_CHANNEL_2", "-1001495022147"))
FORCE_SUB_CHANNEL_3 = int(os.environ.get("FORCE_SUB_CHANNEL_3", "-1001572271892"))
FORCE_SUB_CHANNEL_4 = int(os.environ.get("FORCE_SUB_CHANNEL_4", "-1001723817903"))


TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>𝑯𝒆𝒍𝒍𝒐 {first} 𝒘𝒆𝒍𝒄𝒐𝒎𝒆 𝒕𝒐 @Anime_Eternals 𝒄𝒉𝒂𝒏𝒏𝒆𝒍𝒔....\n\n 𝒀𝒐𝒖 𝒏𝒆𝒆𝒅 𝒕𝒐 𝒋𝒐𝒊𝒏 𝒊𝒏 𝒎𝒚 𝑪𝒉𝒂𝒏𝒏𝒆𝒍/𝑮𝒓𝒐𝒖𝒑 𝒕𝒐 𝒖𝒔𝒆 𝒎𝒆 𝑲𝒊𝒏𝒅𝒍𝒚 𝑷𝒍𝒆𝒂𝒔𝒆 𝒋𝒐𝒊𝒏 𝑪𝒉𝒂𝒏𝒏𝒆𝒍........</b>")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5115691197 6273945163 6103092779 2005714953 5231212075 6497757690").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>𝑯𝒆𝒚!! {mention} 𝒘𝒆𝒍𝒄𝒐𝒎𝒆 𝒕𝒐 @Anime_Eternals 𝒄𝒉𝒂𝒏𝒏𝒆𝒍𝒔\n\n 𝑻𝒐 𝒂𝒄𝒄𝒆𝒔𝒔 𝒕𝒉𝒆𝒔𝒆 𝒇𝒊𝒍𝒆𝒔 𝒚𝒐𝒖 𝒉𝒂𝒗𝒆 𝒕𝒐 𝒋𝒐𝒊𝒏 𝒐𝒖𝒓 𝒄𝒉𝒂𝒏𝒏𝒆𝒍 𝒇𝒊𝒓𝒔𝒕. 𝑷𝒍𝒆𝒂𝒔𝒆 𝒔𝒖𝒃𝒔𝒄𝒓𝒊𝒃𝒆 𝒕𝒐 𝒐𝒖𝒓 𝒄𝒉𝒂𝒏𝒏𝒆𝒍𝒔 𝒕𝒉𝒓𝒐𝒖𝒈𝒉 𝒕𝒉𝒆 𝒃𝒖𝒕𝒕𝒐𝒏𝒔 𝒃𝒆𝒍𝒐𝒘 𝒂𝒏𝒅 𝒕𝒉𝒆𝒏 𝒕𝒂𝒑 𝒐𝒏 𝒕𝒓𝒚 𝒂𝒈𝒂𝒊𝒏 𝒕𝒐 𝒈𝒆𝒕 𝒚𝒐𝒖𝒓 𝒇𝒊𝒍𝒆𝒔\n\n 𝑭𝒐𝒓 𝑶𝒏𝒈𝒐𝒊𝒏𝒈 𝑨𝒏𝒊𝒎𝒆 @Anime_Ongoing_Airings 𝑱𝒐𝒊𝒏 𝑻𝒉𝒊𝒔 𝑪𝒉𝒂𝒏𝒏𝒆𝒍\n\n 𝑻𝒉𝒂𝒏𝒌 𝒀𝒐𝒖.......🍁\n\n » @AnimeNexusNetwork</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!\n\n» ᴍʏ ᴏᴡɴᴇʀ : @KaiXSen"

ADMINS.append(OWNER_ID)
ADMINS.append(6497757690)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
