from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import filters
import os
import random
import logging
from dotenv import load_dotenv
import joke

load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')
USER_ID = int(os.getenv('USER_ID'))
CHAT_ID = int(os.getenv('CHAT_ID'))

logging.basicConfig(level=logging.DEBUG)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

with open('sarcastic_answers.txt', 'r') as data_file:
    answer_var = data_file.readlines()

@dp.message_handler(lambda msg: msg.md_text and msg.md_text.lower().startswith('внимание, анекдот'),
                    content_types=['text'],
                    user_id = USER_ID)
async def sarcastic_reply(message):
    await message.reply(random.choice(answer_var))


@dp.message_handler(content_types=['photo'],
                    user_id = USER_ID)
async def photo_reply(message):
    try:
        if message.md_text and message.md_text.lower().startswith('внимание, анекдот'):
            await message.reply(random.choice(answer_var))
    except TypeError:
        if random.ranint(0,1):
            await message.reply('Не уверен, что это значит, но очень смешно')

@dp.message_handler(commands=['ping'])
async def get_status(message):
    await message.reply('pong')
    
@dp.message_handler(lambda msg: msg.md_text and msg.md_text.lower().startswith('бот, расскажи анекдот'))
async def tell_joke(message):
    await message.reply('Хорошо')
    await message.answer('Внимание, анекдот\n'+joke.get_random_joke())

if __name__=="__main__":
    executor.start_polling(dp, skip_updates=True)
