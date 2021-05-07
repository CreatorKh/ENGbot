import telebot
import config
import random

from telebot import types
bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/Welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    # keyboard
    markup = types.ReplyKeyboardMarkup(row_width=1)
    item1 = types.KeyboardButton("🎲 Рандомное число")
    item2 = types.KeyboardButton("Daily Activities")
    item3 = types.KeyboardButton("Jobs 1")
    item4 = types.KeyboardButton("Jobs 2")
    item5 = types.KeyboardButton("Family")
    item6 = types.KeyboardButton("Actions")
    item8 = types.KeyboardButton("Sports 1")
    item9 = types.KeyboardButton("Sports 2")


    markup.add(item1, item2, item3, item4, item5, item6, item9,item8)

    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, выбери пожалуйста топик.".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)\

@bot.message_handler(commands=['addcard'])
def newcard(message):
    bot.send_message(message.chat.id, "Отправьте флешкарту(фото)")
    if message.photo:
        bot.get_file(message.photo)[-1].file_id.download(f'static/[file_unique_id].jpg')

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == '🎲 Рандомное число':
            bot.send_message(message.chat.id, str(random.randint(0, 100)))
        elif message.text == 'Daily Activities':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("чистить зубы", callback_data='a1')
            item2 = types.InlineKeyboardButton("делать упражнения", callback_data='a2')
            item3 = types.InlineKeyboardButton("одеваться", callback_data='a3')
            item4 = types.InlineKeyboardButton("идти в школу", callback_data='a4')
            item5 = types.InlineKeyboardButton("идти спать", callback_data='a5')
            item6 = types.InlineKeyboardButton("приготовить обед", callback_data='a6')
            item7 = types.InlineKeyboardButton("играть в игры", callback_data='a7')
            item8 = types.InlineKeyboardButton("играть на инструменте", callback_data='a8')
            item9 = types.InlineKeyboardButton("играть в футбол", callback_data='a9')
            item10 = types.InlineKeyboardButton("бегать", callback_data='a10')
            item11 = types.InlineKeyboardButton("учиться", callback_data='a11')
            item12 = types.InlineKeyboardButton("выносить мусор", callback_data='a12')
            item13 = types.InlineKeyboardButton("говорить по телефону", callback_data='a13')
            item14 = types.InlineKeyboardButton("прогулять собаку", callback_data='a14')
            item15 = types.InlineKeyboardButton("помыть руки", callback_data='a15')

            markup.add(item1, item2, item3, item4, item5, item6, item7,item8, item9, item10, item11, item12, item13, item14, item15)

            bot.send_message(message.chat.id, 'WHICH ONE?', reply_markup=markup)

        elif message.text == 'Jobs 1':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("артист", callback_data='b1')
            item2 = types.InlineKeyboardButton("астронавт", callback_data='b2')
            item3 = types.InlineKeyboardButton("шеф повар", callback_data='b3')
            item4 = types.InlineKeyboardButton("дантист", callback_data='b4')
            item5 = types.InlineKeyboardButton("доктор", callback_data='b5')
            item6 = types.InlineKeyboardButton("фермер", callback_data='b6')
            item7 = types.InlineKeyboardButton("пожарный", callback_data='b7')
            item8 = types.InlineKeyboardButton("рыбак", callback_data='b8')
            item9 = types.InlineKeyboardButton("почтальон", callback_data='b9')
            item10 = types.InlineKeyboardButton("музыкант", callback_data='b10')
            item11 = types.InlineKeyboardButton("медсестра", callback_data='b11')
            item12 = types.InlineKeyboardButton("художник", callback_data='b12')
            item13 = types.InlineKeyboardButton("пилот", callback_data='b13')
            item14 = types.InlineKeyboardButton("сотрудник полиции", callback_data='b14')
            item15 = types.InlineKeyboardButton("официант", callback_data='b15')

            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13,
                       item14, item15)

            bot.send_message(message.chat.id, 'WHICH ONE?', reply_markup=markup)

        elif message.text == 'Jobs 2':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("мясник", callback_data='c1')
            item2 = types.InlineKeyboardButton("кассир", callback_data='c2')
            item3 = types.InlineKeyboardButton("тренер", callback_data='c3')
            item4 = types.InlineKeyboardButton("танцор", callback_data='c4')
            item5 = types.InlineKeyboardButton("DJ", callback_data='c5')
            item6 = types.InlineKeyboardButton("цветочник", callback_data='c6')
            item7 = types.InlineKeyboardButton("адвокат", callback_data='c7')
            item8 = types.InlineKeyboardButton("спасатель", callback_data='c8')
            item9 = types.InlineKeyboardButton("шахтер", callback_data='c9')
            item10 = types.InlineKeyboardButton("модель", callback_data='c10')
            item11 = types.InlineKeyboardButton("сантехник", callback_data='c11')
            item12 = types.InlineKeyboardButton("священник", callback_data='c12')
            item13 = types.InlineKeyboardButton("портной", callback_data='c13')
            item14 = types.InlineKeyboardButton("официант", callback_data='c14')
            item15 = types.InlineKeyboardButton("сварщик", callback_data='c15')

            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13,
                       item14, item15)

            bot.send_message(message.chat.id, 'WHICH ONE?', reply_markup=markup)
        elif message.text == 'Family':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("брат", callback_data='d1')
            item2 = types.InlineKeyboardButton("дети", callback_data='d2')
            item3 = types.InlineKeyboardButton("дочь", callback_data='d3')
            item4 = types.InlineKeyboardButton("семья", callback_data='d4')
            item5 = types.InlineKeyboardButton("отец", callback_data='d5')
            item6 = types.InlineKeyboardButton("деда", callback_data='d6')
            item7 = types.InlineKeyboardButton("бабушка", callback_data='d7')
            item8 = types.InlineKeyboardButton("бабушка и дедушка", callback_data='d8')
            item9 = types.InlineKeyboardButton("мама", callback_data='d9')
            item10 = types.InlineKeyboardButton("родители", callback_data='d10')
            item11 = types.InlineKeyboardButton("домашние животные", callback_data='d11')
            item12 = types.InlineKeyboardButton("сестра", callback_data='d12')
            item13 = types.InlineKeyboardButton("сын", callback_data='d13')


            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13)

            bot.send_message(message.chat.id, 'WHICH ONE?', reply_markup=markup)
        elif message.text == 'Actions':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("кусать", callback_data='e1')
            item2 = types.InlineKeyboardButton("подпрыгивать", callback_data='e2')
            item3 = types.InlineKeyboardButton("строить", callback_data='e3')
            item4 = types.InlineKeyboardButton("покупать", callback_data='e4')
            item5 = types.InlineKeyboardButton("разбивать", callback_data='e5')
            item6 = types.InlineKeyboardButton("копать", callback_data='e6')
            item7 = types.InlineKeyboardButton("водить", callback_data='e7')
            item8 = types.InlineKeyboardButton("прятать", callback_data='e8')
            item9 = types.InlineKeyboardButton("поднимать", callback_data='e9')
            item10 = types.InlineKeyboardButton("измерять", callback_data='e10')
            item11 = types.InlineKeyboardButton("подбирать", callback_data='e11')
            item12 = types.InlineKeyboardButton("кататься на велике", callback_data='e12')
            item13 = types.InlineKeyboardButton("трясти", callback_data='e13')
            item14 = types.InlineKeyboardButton("красть", callback_data='e14')
            item15 = types.InlineKeyboardButton("рвать", callback_data='e15')

            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13,
                       item14, item15)

            bot.send_message(message.chat.id, 'WHICH ONE?', reply_markup=markup)
        elif message.text == 'Sports 1':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("стрельба из лука", callback_data='f1')
            item2 = types.InlineKeyboardButton("бейсбол", callback_data='f2')
            item3 = types.InlineKeyboardButton("баскетбол", callback_data='f3')
            item4 = types.InlineKeyboardButton("бобслей", callback_data='f4')
            item5 = types.InlineKeyboardButton("лыжные гонки", callback_data='f5')
            item6 = types.InlineKeyboardButton("езда на велосипеде", callback_data='f6')
            item7 = types.InlineKeyboardButton("дайвинг", callback_data='f7')
            item8 = types.InlineKeyboardButton("горные лыжи", callback_data='f8')
            item9 = types.InlineKeyboardButton("фехтование", callback_data='f9')
            item10 = types.InlineKeyboardButton("фигурное катание", callback_data='f10')
            item11 = types.InlineKeyboardButton("фмериканский футбол", callback_data='f11')
            item12 = types.InlineKeyboardButton("гольф", callback_data='f12')
            item13 = types.InlineKeyboardButton("гимнастика", callback_data='f13')

            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13)

            bot.send_message(message.chat.id, 'WHICH ONE?', reply_markup=markup)
        elif message.text == 'Sports 2':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("хоккей", callback_data='g1')
            item2 = types.InlineKeyboardButton("верховая езда", callback_data='g2')
            item3 = types.InlineKeyboardButton("кикбоксинг", callback_data='g3')
            item4 = types.InlineKeyboardButton("смешанные единоборства", callback_data='g4')
            item5 = types.InlineKeyboardButton("эстафета", callback_data='g5')
            item6 = types.InlineKeyboardButton("бег", callback_data='g6')
            item7 = types.InlineKeyboardButton("скейтбординг", callback_data='g7')
            item8 = types.InlineKeyboardButton("футбол", callback_data='g8')
            item9 = types.InlineKeyboardButton("конькобежный спорт", callback_data='g9')
            item10 = types.InlineKeyboardButton("плавание", callback_data='g10')
            item11 = types.InlineKeyboardButton("теннис", callback_data='g11')
            item12 = types.InlineKeyboardButton("воллейбол", callback_data='g12')
            item13 = types.InlineKeyboardButton("тяжелая атлетика", callback_data='g13')

            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13)

            bot.send_message(message.chat.id, 'WHICH ONE?', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    p = 'static/'
    directory = call.data[0]
    if directory == 'a':
        p += 'daily'
    elif directory == 'b':
        p += 'jobs 1'
    elif directory == 'c':
        p += 'jobs 2'
    elif directory == 'd':
        p += 'family'
    elif directory == 'e':
        p += 'actions'
    elif directory == 'f':
        p += 'sports 1'
    elif directory == 'g':
        p += 'sports 2'



    p+= '/'

    num = call.data[1:]
    p += num + '.jpg'
    try:
        with open(p,'rb') as qq:
            bot.send_photo(call.message.chat.id, qq)
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                  text='Do not forget')

    except Exception as e:
        print(repr(e))

@bot.message_handler(commands=['addcard'])
def newcard(message):
    bot.send_message(message.chat.id, "Отправьте флешкарту(фото)")
    if message.photo:
        bot.get_file(message.photo)[-1].file_id.download('static/[file_id].jpg')






# RUN
bot.polling(none_stop=True)