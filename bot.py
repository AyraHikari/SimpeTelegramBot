import telegram
import requests
import logging
import json
import os

from telegram import ParseMode
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import Filters

# Enable logging
logging.basicConfig(level=logging.INFO)

TOKEN = "Insert your bot token here" # Your bot token from @botfather
CreatorID = 0 # Your ID, see README.md for get your ID

# Use variable system instead if True
Variable = bool(os.environ.get('Var', False))
if Variable:
	TOKEN = os.environ.get('TokenBot', False)
	CreatorID = os.environ.get('MyID', False)
else:
	TOKEN = TOKEN
	CreatorID = CreatorID

bot = telegram.Bot(token=TOKEN)
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

def Start(bot, update):
	update.effective_message.reply_text("Hai!")

def Reply(bot, update):
	msg = update.effective_message.text
	update.effective_message.reply_text(msg)

def SendToCreator(bot, update):
	name = update.effective_message.from_user.first_name
	msg = update.effective_message
	text = update.effective_message.text
	# Use replace method 
	# msg = msg.replace("/feedback ", "") # Disabled
	# Use split method
	text = text.split(None, 1)[1] # Enabled
	chat_id = update.effective_chat.id
	message = "*New* `1` message from [{name}](tg://user?id={id})\n\n{message}".format(name=name, \
		id=msg.from_user.id, message=text)
	bot.sendMessage(CreatorID, message, parse_mode=ParseMode.MARKDOWN)
	update.effective_message.reply_text("Message was sent!")

def Log(bot, update):
	message = update.effective_message
	eventdict = message.to_dict()
	jsondump = json.dumps(eventdict, indent=4)
	update.effective_message.reply_text(jsondump)


start_handler = CommandHandler("start", Start)
reply_handler = CommandHandler("reply", Reply)
feedback_handler = CommandHandler("feedback", SendToCreator)
logger_handler = CommandHandler("log", Log)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(reply_handler)
dispatcher.add_handler(feedback_handler)
dispatcher.add_handler(logger_handler)

__log__ = logging.getLogger()
__log__.info("Running bot success!")
updater.start_polling()
