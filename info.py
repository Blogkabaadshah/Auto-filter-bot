import re
import os
from os import environ
from Script import script

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

#main variables
API_ID = int(environ.get('API_ID', '25680646'))
API_HASH = environ.get('API_HASH', '0a403b1d2ac0aa5ba34a2fab2ba6a12b')
BOT_TOKEN = environ.get('BOT_TOKEN', '7125124679:AAF1HHGWwU1lE9xPZtolENRxsBb_ZbftYys')

ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6964743059').split()]
USERNAME = environ.get('USERNAME', "https://t.me/Moviegurusupport")
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002188008502'))
MOVIE_GROUP_LINK = environ.get('MOVIE_GROUP_LINK', 'https://t.me/moviesguru_requestgrp')
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002443223307').split()]
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://Blog:eCXh29bITQQS0rrm@cluster0.s1aaq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DATABASE_NAME = environ.get('DATABASE_NAME', "clusterblog")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'blogfiles')
LOG_API_CHANNEL = int(environ.get('LOG_API_CHANNEL', '-1002188008502'))
QR_CODE = environ.get('QR_CODE', 'https://graph.org/file/c3257557a3e82819ffe5c-4afd0202e555c8aed1.jpg')
START_IMG = environ.get('START_IMG', 'https://graph.org/file/4e61ac07588f4989248b2-e6cfe55a6cbe8fa632.jpg')
BIN_CHANNEL = int(environ.get('BIN_CHANNEL','-1002188008502'))
DELETE_CHANNELS = int(environ.get('DELETE_CHANNELS','-1002188008502'))
URL = environ.get('URL', 'https://awkward-anastasia-sayandip-f4c355c8.koyeb.app/')
STICKERS_IDS = ('CAACAgQAAxkBAAEK99dlfC7LDqnuwtGRkIoacot_dGC4zQACbg8AAuHqsVDaMQeY6CcRojME').split()
FILE_AUTO_DEL_TIMER = int(environ.get('FILE_AUTO_DEL_TIMER', '600'))
IS_VERIFY = is_enabled('IS_VERIFY', True)
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', '-1002188008502'))
TUTORIAL = environ.get("TUTORIAL", "https://t.me/Moviegurusupport/13")
VERIFY_IMG = environ.get("VERIFY_IMG", "https://graph.org/file/d122da13cf9dcdeb7c4b1-83371b1b73d408e0fb.jpg")
SHORTENER_API = environ.get("SHORTENER_API", "2adc64232463a656cb4f7476e4fb0ce2dc418feb")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", 'ShortXLinks.com')
SHORTENER_API2 = environ.get("SHORTENER_API2", "19df554dcfbb6b33544301d6618e0ce6ca3084c1")
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", 'Gplinks.com')
SHORTENER_API3 = environ.get("SHORTENER_API3", "e13d1324ecdd75f04a0ab5ead11d52d215585abd")
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", 'Omegalinks.in')
TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "1200"))
THREE_VERIFY_GAP = int(environ.get('THREE_VERIFY_GAP', "86400"))

LANGUAGES = ["hindi", "english", "telugu", "tamil", "kannada", "malayalam", "bengali", "marathi", "gujarati", "punjabi"]
QUALITIES = ["HdRip","web-dl" ,"bluray", "hdr", "fhd" , "240p", "360p", "480p", "540p", "720p", "960p", "1080p", "1440p", "2K", "2160p", "4k", "5K", "8K"]
YEARS = [f'{i}' for i in range(2024 , 2002,-1 )]
SEASONS = [f'season {i}'for i in range (1 , 23)]
REF_PREMIUM = 100
PREMIUM_POINT = 1500
auth_channel = environ.get('AUTH_CHANNEL', '-1002466967695')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
SUPPORT_GROUP = int(environ.get('SUPPORT_GROUP', '-1002489973303'))
request_channel = environ.get('REQUEST_CHANNEL', '-1002188008502')
REQUEST_CHANNEL = int(request_channel) if request_channel and id_pattern.search(request_channel) else None
UPI_PAY_LOGS = int(environ.get('UPI_PAY_LOGS', '-1002188008502'))
MOVIE_UPDATE_CHANNEL = int(environ.get('MOVIE_UPDATE_CHANNEL', '-1002425005337'))

AUTO_FILTER = is_enabled('AUTO_FILTER', True)
PORT = os.environ.get('PORT', '5000')
MAX_BTN = int(environ.get('MAX_BTN', '8'))
AUTO_DELETE = is_enabled('AUTO_DELETE', True)
DELETE_TIME = int(environ.get('DELETE_TIME', 1200))
IMDB = is_enabled('IMDB', True)
FILE_CAPTION = environ.get('FILE_CAPTION', f'{script.FILE_CAPTION}')
IMDB_TEMPLATE = environ.get('IMDB_TEMPLATE', f'{script.IMDB_TEMPLATE_TXT}')
LONG_IMDB_DESCRIPTION = is_enabled('LONG_IMDB_DESCRIPTION', False)
PROTECT_CONTENT = is_enabled('PROTECT_CONTENT', False)
SPELL_CHECK = is_enabled('SPELL_CHECK', True)
LINK_MODE = is_enabled('LINK_MODE', True)
SETTINGS = {
            'spell_check': SPELL_CHECK,
            'auto_filter': AUTO_FILTER,
            'file_secure': PROTECT_CONTENT,
            'auto_delete': AUTO_DELETE,
            'template': IMDB_TEMPLATE,
            'caption': FILE_CAPTION,
            'tutorial': TUTORIAL,
            'shortner': SHORTENER_WEBSITE,
            'api': SHORTENER_API,
            'shortner_two': SHORTENER_WEBSITE2,
            'api_two': SHORTENER_API2,
            'log': LOG_VR_CHANNEL,
            'imdb': IMDB,
            'link': LINK_MODE, 
            'is_verify': IS_VERIFY, 
            'verify_time': TWO_VERIFY_GAP,
            'shortner_three': SHORTENER_WEBSITE3,
            'api_three': SHORTENER_API3,
            'third_verify_time': THREE_VERIFY_GAP
    }
DEFAULT_POST_MODE = {
    'singel_post_mode' : False,
    'all_files_post_mode' : False
}
