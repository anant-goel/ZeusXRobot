# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open('{}/ZeusXRobot/{}'.format(os.getcwd(), config),
              'r') as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    #Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 17372560  # integer value, dont use ""
    API_HASH = "e4d5f831cc33652445762eaf8a83aa62"
    TOKEN = "5271886587:AAHL6G8-k0w7oC65YiNLf6R95oDfj4FiuKo"  #This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 873948892  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "Anant_Goel"
    SUPPORT_CHAT = 'PcGamesAllForFree'  #Your own group for support, do not add the @
    UPDATES_CHANNEL = 'PcGamesAllForFree' #Your own channel for Updates of bot, Do not add @
    JOIN_LOGGER = -1001737747308  #Prints any new group the bot is added to, prints just the name and ID.
    REM_BG_API_KEY = "uUbTxFRLRQdJ4uMMwxkdWEZo"
    TEMP_DOWNLOAD_DIRECTORY = ""
    EVENT_LOGS = -793784681  #Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    SQLALCHEMY_DATABASE_URI = '' #do you hub your old heroku app database_URL then put here, most use 25days ago sql
    LOAD = [] #try to kang this db ur big mothersfuckers i know your noob so only kanging my db
    NO_LOAD = ['rss', 'cleaner', 'connection', 'math']
    WEBHOOK = None
    INFOPIC = True
    URL = None
    SPAMWATCH_API = ""  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"
    BOT_USERNAME = "steamunlockedgroupbot"
    BOT_ID = "5271886587"
    
    DRAGONS = get_user_list('elevated_users.json', 'sudos')

    DEV_USERS = get_user_list('elevated_users.json', 'devs')
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list('elevated_users.json', 'supports')
    #List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list('elevated_users.json', 'tigers')
    WOLVES = get_user_list('elevated_users.json', 'whitelists')
    DONATION_LINK = https://t.me/PcGamesAllForFree # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  #Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    STRICT_GMUTE = True
    WORKERS = 8  # Number of subthreads to use. Set as number of threads your processor uses
    BAN_STICKER = 'CAACAgQAAx0CU_rCTAABAczQXyBOv1TsVK4EfwnkCUT1H0GCkPQAAtwAAwEgTQaYsMtAltpEwhoE'  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    ARQ_API_URL = "https://thearq.tech"
    ARQ_API_KEY = "YIECCC-NAJARO-OLLREW-SJSRIP-ARQ"
    CASH_API_KEY = '7O0TUX4ITJQUVXWC'  # Get your API key from https://www.alphavantage.co/support/#api-key
    TIME_API_KEY = 'IZW26DEW90AI'  # Get your API key from https://timezonedb.com/api
    OPENWEATHERMAP_ID = '92e7f4437ef3cebd55c3a3cec379edca'
    WALL_API = ''  #For wallpapers, get one from https://wall.alphacoders.com/api.php
    AI_API_KEY = '9a43a0f251cd1f5366dba5502df57843e926acfd653b4e3f53a4ba49fec6b3732b25fb389ec1aa1d702c9238d10c5e2ce3506758dc3fce5f278d333775787eca'  #For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
