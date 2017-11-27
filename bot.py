 #-*- coding: utf-8 -*-
import config
import datetime
import telebot
import random
from telebot import types
from telebot import types

bot = telebot.TeleBot(config.token)

hleb = ["https://www.youtube.com/watch?v=OvZUf7YOBmU",
		"https://www.youtube.com/watch?v=UMfMekip6y8",
		"https://www.youtube.com/watch?v=1lBsJDludgI"]


		
@bot.message_handler(commands=['start', 'help'])



#def henn(message):
#	bot.send_message(message.chat.id, 'ваше видео, повелитель!')
#	#bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=OvZUf7YOBmU')
#	bot.send_message(message.chat.id, random.choice(hleb))


#if __name__ == '__main__':
#     bot.polling(none_stop=True)

def henn(message):
	i = 1
	while  i < 1000000:
		bot.send_message(message.chat.id, 'Саша мосин Говноед лоханский')
		pass

if __name__ == '__main__':
     bot.polling(none_stop=True)