# telegram-bot
import time
from gettext import translation

import telebot
import random
from telebot import types
import os

TELEGRAM_API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')

bot = telebot.TeleBot(TELEGRAM_API_TOKEN)
user_scores = {}

words = {
    'apple': 'яблоко',
    'banana': 'банан',
    'cherry': 'вишня',
    'dog': 'собака',
    'cat': 'кот',
    'house': 'дом',
    'tree': 'дерево',
    'car': 'машина',
    'sun': 'солнце',
    'moon': 'луна',
    'star': 'звезда',
    'bird': 'птица',
    'fish': 'рыба',
    'book': 'книга',
    'pen': 'ручка',
    'table': 'стол',
    'chair': 'стул',
    'computer': 'компьютер',
    'phone': 'телефон',
    'window': 'окно',
    'door': 'дверь',
    'shoe': 'туфля',
    'sock': 'носок',
    'shirt': 'рубашка',
    'jacket': 'куртка',
    'hat': 'шляпа',
    'glove': 'перчатка',
    'water': 'вода',
    'bread': 'хлеб',
    'milk': 'молоко',
    'tea': 'чай',
    'coffee': 'кофе',
    'juice': 'сок',
    'salt': 'соль',
    'sugar': 'сахар',
    'meat': 'мясо',
    'fruit': 'фрукты',
    'vegetable': 'овощи',
    'chicken': 'курица',
    'beef': 'говядина',
    'pizza': 'пицца',
    'hamburger': 'гамбургер',
    'cake': 'торт',
    'cookie': 'печенье',
    'ice cream': 'мороженое',
    'chocolate': 'шоколад',
    'cheese': 'сыр',
    'egg': 'яйцо',
    'butter': 'масло',
    'flour': 'мука',
    'soup': 'суп',
    'sandwich': 'бутерброд',
    'salad': 'салат',
    'pasta': 'паста',
    'rice': 'рис',
    'potato': 'картофель',
    'tomato': 'помидор',
    'onion': 'лук',
    'garlic': 'чеснок',
    'pepper': 'перец',
    'carrot': 'морковь',
    'cucumber': 'огурец',
    'lettuce': 'салат',
    'orange': 'апельсин',
    'lemon': 'лимон',
    'grape': 'виноград',
    'melon': 'дыня',
    'pear': 'груша',
    'strawberry': 'клубника',
    'blueberry': 'черника',
    'raspberry': 'малина',
    'blackberry': 'ежевика',
    'peach': 'персик',
    'apricot': 'абрикос',
    'plum': 'слива',
    'kiwi': 'киви',
    'mango': 'манго',
    'pineapple': 'ананас',
    'watermelon': 'арбуз',
    'grapefruit': 'грейпфрут',
    'coconut': 'кокос',
    'fig': 'инжир',
    'cantaloupe': 'канталупа',
    'broccoli': 'брокколи',
    'spinach': 'шпинат',
    'zucchini': 'кабачок',
    'eggplant': 'баклажан',
    'pumpkin': 'тыква',
    'apron': 'фартук',
    'bag': 'сумка',
    'watch': 'часы',
    'belt': 'пояс',
    'ring': 'кольцо',
    'bracelet': 'браслет',
    'necklace': 'ожерелье',
    'glasses': 'очки',
    'scarf': 'шарф',
    'shoes': 'обувь',
    'boots': 'сапоги',
    'sandals': 'сандалии',
    'umbrella': 'зонт',
    'glove': 'перчатка',
    'sweater': 'свитер',
    'jeans': 'джинсы',
    'shorts': 'шорты',
    'skirt': 'юбка',
    'dress': 'платье',
    't-shirt': 'футболка',
    'coat': 'пальто',
    'suit': 'костюм',
    'tie': 'галстук',
    'scarf': 'шарф',
    'socks': 'носки'
}


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, f'Привет! 🌟 Я помогу тебе учить английские слова. Вот что ты можешь делать: \n'
                         f'/learn — учи новые слова \n'
                         f'/score — проверь свой прогресс \n'
                         f'/game — играй и проверяй знания \n'
                         f'/help — получи помощь \n'
                         f'Давай начнем! 🚀')
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton("Начать изучать слова", callback_data="start_learning")
    markup.add(button)

    bot.send_message(message.chat.id, "Привет! Нажми кнопку, чтобы начать учить слова.", reply_markup=markup)
@bot.callback_query_handler(func=lambda call: call.data == 'start_learning')
def button(call):
    bot.send_message(call.message.chat.id, 'Начинаем учить слова! Напиши /learn')
    # bot.register_next_step_handler(call, learn)
@bot.message_handler(commands=['learn'])
def learn(message):
    word, translation = random.choice(list(words.items()))
    bot.send_message(message.chat.id, f"📝 Слово для изучения: {word}")
    time.sleep(1)
    bot.send_message(message.chat.id, f'✅ Перевод: {translation}. Напишите /learn, чтобы продолжить.')

@bot.message_handler(commands=['game'])
def game(message):
    word, translation = random.choice(list(words.items()))
    bot.send_message(message.chat.id, f'Как переводится слово: {word}?')
    bot.register_next_step_handler(message, check_answers, translation)

def check_answers(message, correct_answer):
    user_id = message.chat.id
    if user_id not in user_scores:
        user_scores[user_id] = 0

    if message.text.lower() == correct_answer.lower():
        user_scores[user_id] += 1
        bot.send_message(message.chat.id, 'Правильно!🎉 Напиши /game, чтобы сыграть еще раз')

    else:
        bot.send_message(message.chat.id, f"Неправильно!❌ Правильный ответ: {correct_answer}. "
                                          f"Попробуй еще раз: /game")



@bot.message_handler(commands=['score'])
def score(message):
    user_id = message.chat.id
    score = user_scores.get(user_id, 0)
    bot.send_message(message.chat.id, f'Ваши очки: {score} 🏆 ')



@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, 'В разработке')


bot.polling()
