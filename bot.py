from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import filters
import os
import random
import logging
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')
USER_ID = int(os.getenv('USER_ID'))

logging.basicConfig(level=logging.DEBUG)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

answer_var = (
        'АХАХАХАХ ТЫ ТАКОЙ СМЕШНОЙ',
        'ДАВАЙ ЕЩЕ АНЕКДОТ',
        'И ГДЕ ТЫ ТОЛЬКО ТАКИЕ ШУТКИ НАХОДИШЬ',
        'А ТЫ СЛУЧАЙНО НЕ СТЕНДАП-КОМИК', 
        'МОЖЕШЬ ЕЩЕ ПОШУТИТЬ', 
        'А ТЫ СЛУЧАЙНО В КВН НЕ УЧАСТВОВАЛ',
        'КАКОЙ СМЕШНОЙ МАЛЬЧИК'
        )

@dp.message_handler(lambda msg: msg.md_text and msg.md_text.lower().startswith('внимание, анекдот'),
                    content_types=['text'],
                    user_id = USER_ID)
async def sarcastic_reply(message):
    await message.reply(random.choice(answer_var))


@dp.message_handler(content_types=['photo'],
                    user_id = USER_ID)
async def sarcastic_reply(message):
    try:
        if message.md_text and message.md_text.lower().startswith('внимание, анекдот'):
            await message.reply(random.choice(answer_var))
    except TypeError:
        await message.reply('Не уверен, что это значит, но очень смешно')

@dp.message_handler(commands=['ping'])
async def get_status(message):
    await message.reply('pong')

if __name__=="__main__":
    executor.start_polling(dp, skip_updates=True)
