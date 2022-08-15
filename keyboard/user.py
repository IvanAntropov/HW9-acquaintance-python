from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('/start')
b3 = KeyboardButton('/help')

kb_user = ReplyKeyboardMarkup(resize_keyboard=True) 

kb_user.add(b1).add(b3)



