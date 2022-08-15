import logging
import pytube
from aiogram import Bot, Dispatcher
from aiogram import types
from aiogram import executor
from keyboard.user import kb_user
# from pytube import YouTube

logging.basicConfig(level=logging.INFO)

async def bot_on(_):
    print('Bot is on...')

API_TOKEN = 'token'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start','help'])
async def send_welcome(message: types.Message):
    await message.reply("Приветсвую, я бот, который качает видео с youtube.\n\
Для этого напиши комманду и ввставь ссылку через пробел: \n\
/video https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley\n\
Для указания директории, вводи:\n\
/direct \downloads", reply_markup=kb_user)
        
@dp.message_handler(commands='video')
async def video(message: types.Message):
    try:
        global direct 
        listHelp = message.text.split(' ')
        link = listHelp[1]
        vid = pytube.YouTube(link)
        await message.answer('Downloading: ', vid.title)
        vid_download = vid.streams.get_by_itag('18')
        vid_download.download(direct) 
    except ValueError:
        await message.answer("Что-то пошло не так. Пробуй снова!")
        
@dp.message_handler(commands='direct')
async def video(message: types.Message):
    try:
        listHelp = message.text.split(' ')
        global direct 
        direct = listHelp[1] 
    except ValueError:
        await message.answer("Что-то пошло не так. Пробуй снова!")
        
@dp.message_handler()
async def echo(message: types.Message):
    await message.answer('Я - бот, умеющий только качать видео с youtube.')
    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=bot_on)