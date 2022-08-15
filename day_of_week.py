import logging
from aiogram import Bot, Dispatcher
from aiogram import types
from aiogram import executor
from keyboard.user import kb_user

logging.basicConfig(level=logging.INFO)

async def bot_on(_):
    print('Bot is on...')

API_TOKEN = 'token'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start','help'])
async def send_welcome(message: types.Message):
    await message.reply("Приветсвую, я бот, который только и знает, что говорить какой день недели выходной, а какой нет!\n\
Для этого напиши комманду и число дня недели: \n\
/day 5", reply_markup=kb_user)

@dp.message_handler(commands='day')
async def start_ex1(message: types.Message):
    try:
        listHelp = message.text.split(' ')
        number = int(listHelp[1])
        if number > 7 or number < 1:
            await message.answer("В неделе 7 дней.")
        else:
            if number == 6 or number == 7:
                await message.answer(f'{number} -> weekend')
            else:
                await message.answer(f'{number} -> weekdays')                  
    except ValueError:
        await message.answer("Цифры вводи, дурень!")
        
@dp.message_handler(commands='video')
async def video(message: types.Message):
    await bot.send_video(message.chat.id, open('data\hitler and puppits.mp4', 'rb'))
        
@dp.message_handler()
async def echo(message: types.Message):
    await message.answer('Я - бот, умеющий только говорить, какой день недели выходной. Ну м могу видео отправить)\n\
/video')
    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=bot_on)
