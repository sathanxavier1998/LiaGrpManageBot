import os

from dotenv import load_dotenv

load_dotenv("config.env" if os.path.isfile("config.env") else "sample_config.env")

BOT_TOKEN = os.environ.get('BOT_TOKEN', "2003104605:AAEuBiBNsZQz7e9qBE2EGxG8yoEILtIf_44")
API_ID = int(os.environ.get('API_ID', "6620972"))
SESSION_STRING = os.environ.get('SESSION_STRING', 'BQBlBywARkI7254FGPuJS56_htSYkZEjqD2D7pQYWGGxqNHBj05lNJqAa-w7s2KRzKKGVHXmvN9Rfp_r3bp55z6YZDzxsqZNXgRFnztazl8ORGC4v-eDXsxHRqtXvWMDxsrKNyVIZOIPkDeDWRSOt-h5qcpmrCGER-S3fK9o-0OhxGViVx6OO8tNeJeMK5BmgGgPOEFWL_pYER_axEqMTRMRC0T_UDKQXtIzMmsRIZmtzFrXE_LGd6Yhy6yR0ivuOrcUTnfQshrE2ztf23eZPlHeMr28U7ZGOQd07PYs67tWUmIHL9-Fvlp8gSx8UFEAKgABfgtjsL_GzgWzhj6RkB12Ck97SgAAAABoA08GAA')
API_HASH = os.environ.get('API_HASH', "3f6835286b03e000ab6d71b37cc35b92")
USERBOT_PREFIX = os.environ.get('USERBOT_PREFIX', '.')
PHONE_NUMBER = os.environ.get('PHONE_NUMBER', '')
SUDO_USERS_ID = list(map(int, os.environ.get('SUDO_USERS_ID', '6047510747').split()))
LOG_GROUP_ID = int(os.environ.get('LOG_GROUP_ID', '-1001696127730'))
GBAN_LOG_GROUP_ID = int(os.environ.get('GBAN_LOG_GROUP_ID', '-1001696127730'))
MESSAGE_DUMP_CHAT = int(os.environ.get('MESSAGE_DUMP_CHAT', '-1001696127730'))
WELCOME_DELAY_KICK_SEC = int(os.environ.get('WELCOME_DELAY_KICK_SEC', 600))
MONGO_URL = os.environ.get('MONGO_URL', "mongodb+srv://MV:MV@cluster0.rfx5f4x.mongodb.net/?retryWrites=true&w=majority")
ARQ_API_KEY = os.environ.get('ARQ_API_KEY')
ARQ_API_URL = os.environ.get('ARQ_API_URL', 'https://arq.hamker.in')
LOG_MENTIONS = os.environ.get('LOG_MENTIONS', 'True').lower() in ['true', '1']
RSS_DELAY = int(os.environ.get('RSS_DELAY', 300))
PM_PERMIT = os.environ.get('PM_PERMIT', 'True').lower() in ['true', '1']
