import telebot
import pyowm
owm = pyowm.OWM('af58f9550e517a9bfd3a9598fa63148f', language = "ru" )
bot = telebot.TeleBot("962681741:AAEMeFM85tdqHlvcTSpTdZqV8evBJSdRXLE")
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id,"Ведите город или страну")
@bot.message_handler(content_types=['text'])

def send_echo(message):
	#bot.reply_to(message, message.text)	
	
	observation = owm.weather_at_place(message.text)
	w = observation.get_weather()
	temp=w.get_temperature('celsius')["temp"]

	answer="В городе или в стране "+message.text+" сейчас "+w.get_detailed_status()+"\n"
	answer+="Температура сейчас в районе"+str(temp)+"\n"

	if temp<10:
		answer+="Сейчас очень холодно , одевайся как танк"
	elif temp<20:
		answer+="Сейчас прохлодно оденься по теплее"
	else:
		answer+="Сейчас норм наденься как хочешь"



	bot.send_message(message.chat.id,answer)


@bot.message_handler(content_types=['text'])
def lala2(message):
	bot.send_message(message.chat.id,message.text)

bot.polling(none_stop = True)