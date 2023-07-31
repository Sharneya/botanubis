import telebot
from dotenv import load_dotenv
import os

load_dotenv()
bot = telebot.TeleBot(os.getenv('TOKEN'))
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Добрый вечер. Отправьте команду')

@bot.message_handler()
def ger_user_text(message):
    if message.text == "password":
        bot.send_message(message.chat.id, 'Ваш пароль: user.anubis402')
    elif 'информ'in message.text:
        bot.send_message(message.chat.id, 'Отправьте фамилию, имя и отчество человека')
        if ('Мурова' in message.text) and (('Алёна' in message.text) or ("Алена" in message.text)) and ('Михайловна' in message.text):
            photo = open('murova.jpg', 'rb')
            bot.send_photo(message.chat.id, photo)
        elif 'Андреева' in message.text and 'Екатерина' in message.text and 'Петрвона' in message.text:
            bot.send_message(message.chat.id, 'Данный пользователь защищен. Информация засекречена')
'''
    else:






    elif "Мурова"  in message.text:
        bot.send_message(message.chat.id, 'Последнее фото сделано в 23:00 о мск')
    else:
        bot.send_message(message.chat.id, 'Данные об этом человеке не найдены. Проверьте корректность имени.')
'''
bot.polling(none_stop=True)