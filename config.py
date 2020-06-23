from twitchio.ext import commands



TMI_TOKEN = ''
CLIENT_ID = ''
BOT_NICK = 'owlbot'
BOT_PREFIX = '!'
CHANNEL = ['']

bot = commands.Bot(
    irc_token = TMI_TOKEN ,
    client_id = CLIENT_ID ,
    nick = BOT_NICK ,
    prefix = BOT_PREFIX ,
    initial_channels = CHANNEL
	)