#библиотеки, которые загружаем из вне
import telebot
TOKEN = 'токен скрыт'

from telebot import types

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('welcome.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)

	#клавиатура
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("🦾 Мой репозиторий")
	item2 = types.KeyboardButton("✍️ Написать мне в личку")
	item3 = types.KeyboardButton("😍Чек-листы")
	item4 = types.KeyboardButton("🤮QA black list")


	markup.add(item1, item2, item3, item4)

	bot.send_message(message.chat.id, "Приветствую, {0.first_name}!".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

#назначаем действие для клавиатуры
@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == '🦾 Мой репозиторий':
			bot.send_message(message.chat.id, 'https://github.com/Rick-Styler')
		elif message.text == '✍️ Написать мне в личку':
			bot.send_message(message.chat.id, 'http://t.me/Rick_Styler')
		if message.text == '👌Мои чек-листы':
			bot.send_message(message.chat.id, 'https://miro.com/app/board/uXjVO9YDsNc=/?share_link_id=456580442150')
		if message.text == '😑Black list it компаний':
			bot.send_message(message.chat.id, 'https://t.me/qa_bad_company')
		else:
			bot.send_message(message.chat.id, '🚫Что-то пошло не так, не знаю как ответить на ваш запрос😓')


bot.polling(none_stop=True)









#https://core.telegram.org/bots/api#available-methods
