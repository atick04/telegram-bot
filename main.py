

from subprocess import call
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ 5320085206:AAGePDg1W9nyfzEr55Ui2m-xCMGwcwad34o CHARISMA_BOT///////////////////////////////////////////////////
# 5362949107:AAGUjh8X-_eq2FE2OH6n9yCGQgcoyAA0mU8 my test bot
import telebot

bot = telebot.TeleBot('5320085206:AAGePDg1W9nyfzEr55Ui2m-xCMGwcwad34o')


@bot.message_handler(commands=['start'])
def start(message):
    user = message.chat.first_name
    file = open('Вступление.mp3', 'rb')
    otvet = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton("Открыть доступ 🔐", callback_data="Open dostup")
    otvet.add(button1)
    bot.send_audio(message.chat.id, file, reply_markup=otvet,
                   caption=f"\nЗдравствуй, {user}, мы рады видеть тебя в наших рядах!\n"

                           "\nС нами ты прокачаешь свою харизму и станешь уверенным в себе человеком, а также по окончании курса получишь два очень крутых бонуса! 🎁\n"

                           "\nЭто голосовое для тебя. " "Послушай его и осознай, что всё это может стать реальностью, и ты как никогда близок к этому!\n"

                           "*\nЖми на кнопку ниже и мы отправим тебе обучение ⤵️\n*", parse_mode="Markdown")


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    otvet2 = types.InlineKeyboardMarkup(row_width=1)
    button2 = types.InlineKeyboardButton("Готово ✅", callback_data="Done")
    otvet2.add(button2)
    if call.data == "Open dostup":
        bot.send_message(call.message.chat.id,
                         'Вот это уже другое дело! Видно, ты настроен решительно. Но прежде чем начать обучение, просто подпишись на не менее полезные каналы:\n'

                          '\n[1. Апгрейд | Мотивация](https://t.me/+0PaizJSIfVNhNmRi)\n'
                         '[2. Сила Разума](https://t.me/+rOUcGQRjsmpjN2Uy)\n'
                         '[3. Подкасты | Аудиокниги](https://t.me/+79LApShMD7U2NjIy)\n'
                         '[4. Тив Жобс](https://t.me/+Yhb37VnrI-oxZTli)\n'
                         '[5. Business People](https://t.me/+FKlcY8qwXyAwMTU0)\n'

                         '\nБольше ничего не нужно. Всё, что произойдёт с тобой дальше – это история. История, которую ты будешь вспоминать и которой будешь гордиться долгие годы.',
                         parse_mode="Markdown", reply_markup=otvet2, disable_web_page_preview=True)

    if call.data == "Done":
        status = ['creator', 'administrator', 'member']
        for i in status:
            if i == bot.get_chat_member(chat_id=(-1001151167268), user_id=call.message.chat.id).status:
              
                check_1(call)
                break
        else:
                  bot.answer_callback_query(callback_query_id=call.id, text= "Вы не подписаны на 1-й канал")
       

def check_1(call):   
        status = ['creator', 'administrator', 'member']
        for i in status:
            if i == bot.get_chat_member(chat_id=(-1001575996988), user_id=call.message.chat.id).status:
                
                check_2(call)
                break
        else:
                  bot.answer_callback_query(callback_query_id=call.id, text= "Вы не подписаны на 2-ой канал")

def check_2(call):    
        status = ['creator', 'administrator', 'member']
        for i in status:
            if i == bot.get_chat_member(chat_id=(-1001474810841), user_id=call.message.chat.id).status: 
                
                check_3(call)
                break
        else:
                  bot.answer_callback_query(callback_query_id=call.id, text= "Вы не подписаны на 3-й канал")

def check_3(call):    
        status = ['creator', 'administrator', 'member']
        for i in status:
            if i == bot.get_chat_member(chat_id=(-1001222810814), user_id=call.message.chat.id).status:
               
                check_4(call)
                break
        else:
                  bot.answer_callback_query(callback_query_id=call.id, text= "Вы не подписаны на 4-ый канал")

def check_4(call):         
        status = ['creator', 'administrator', 'member']
        for i in status:
            if i == bot.get_chat_member(chat_id=(-1001214791785), user_id=call.message.chat.id).status:
                bot.answer_callback_query(callback_query_id=call.id, text='Вы подписаны на все каналы!')
                
                break
        else:
                  bot.answer_callback_query(callback_query_id=call.id, text= "Вы не подписаны на 5-ый канал")






        if call.data == "Done":
            otvet3 = types.InlineKeyboardMarkup(row_width=1)
            button3 = types.InlineKeyboardButton("Следующий модуль 🔑", callback_data="Next")
            otvet3.add(button3)
            file = open('CHARISMA_PHOTO\@xapizma_bot1.png','rb')
            bot.send_photo(call.message.chat.id,file,
                                '*\nМодуль 1: Слушаем больше, чем говорим.\n*'

                                '\nЗадаем вопросы. Поддерживаем зрительный контакт. Улыбаемся. Отвечаем не только словами, но и невербально. Так мы показываем другому человеку, что он важен.\n'

                                '\nНе даем советов, если нас об этом не просят. Говорим только тогда, когда должны сказать что-то важное для человека, а не только для нас.\n'

                                '*\nНе забывай, что дойдя до конца, ты получишь два крутых бонуса 🎁\n*',parse_mode="Markdown",reply_markup=otvet3)
@bot.callback_query_handler(func=lambda call: True)
def callback_call(call):
        if call.data == "Next":
            otvet4 = types.InlineKeyboardMarkup(row_width=1)
            button4 = types.InlineKeyboardButton("next 🔑", callback_data="Next_module")
            otvet4.add(button4)
            file = open('CHARISMA_PHOTO\@xapizma_bot2.png','rb')
            bot.send_photo(call.message.chat.id,file,
                                '*\nМодуль 1: Слушаем больше, чем говорим.\n*'

                                '\nЗадаем вопросы. Поддерживаем зрительный контакт. Улыбаемся. Отвечаем не только словами, но и невербально. Так мы показываем другому человеку, что он важен.\n'

                                '\nНе даем советов, если нас об этом не просят. Говорим только тогда, когда должны сказать что-то важное для человека, а не только для нас.\n'

                                '*\nНе забывай, что дойдя до конца, ты получишь два крутых бонуса 🎁\n*',parse_mode="Markdown",reply_markup=otvet4)

                          
        



bot.polling(none_stop=True)


