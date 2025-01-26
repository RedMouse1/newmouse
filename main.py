from config import TOKEN
import telebot
import random  # Импортируем модуль random для выбора случайной шутки, цитаты и факта

bot = telebot.TeleBot(TOKEN)

# Список шуток
jokes = [
    "Почему программисты не любят природу? Потому что в ней слишком много багов.",
    "Какой язык программирования самый оптимистичный? Python, потому что он всегда возвращает 'True'.",
    "Почему Java разработчики предпочитают темные комнаты? Потому что они не могут найти 'null'.",
    "Какой любимый напиток программиста? Java!",
]

# Список мудрых цитат
quotes = [
    "Жизнь — это то, что происходит, пока вы заняты строить другие планы. — Джон Леннон",
    "Сложности — это просто возможность проявить свои лучшие качества. — Уинстон Черчилль",
    "Не бойтесь делать ошибки. Учитесь на них. — Ричард Бренсон",
    "Секрет успеха в том, чтобы начать. — Марк Твен",
]

# Список интересных фактов
facts = [
    "Человеческий мозг состоит на 75% из воды.",
    "Слон — единственное животное, которое не может прыгать.",
    "Кошки могут делать прыжки в 6 раз длиннее своего тела.",
    "У осьминога три сердца.",
]

# Хэндлер для команд '/start' и '/mouse'
@bot.message_handler(commands=['start', 'mouse'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi, I am Mouse!\
""")

# Хэндлер для команды '/joke'
@bot.message_handler(commands=['joke'])
def send_joke(message):
    joke = random.choice(jokes)  # Выбираем случайную шутку из списка
    bot.reply_to(message, joke)  # Отправляем шутку пользователю

# Хэндлер для команды '/quote'
@bot.message_handler(commands=['quote'])
def send_quote(message):
    quote = random.choice(quotes)  # Выбираем случайную цитату из списка
    bot.reply_to(message, quote)  # Отправляем цитату пользователю

# Хэндлер для команды '/fact'
@bot.message_handler(commands=['fact'])
def send_fact(message):
    fact = random.choice(facts)  # Выбираем случайный факт из списка
    bot.reply_to(message, fact)  # Отправляем факт пользователю

bot.infinity_polling()