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

# @dp.message_handler(user_id = USER_ID)
@dp.message_handler(lambda msg: msg.md_text.lower().startswith('внимание, анекдот'),
                    user_id = USER_ID)
async def sarcastic_reply(message):
    await message.reply(random.choice(answer_var))


@dp.message_handler(lambda msg: msg.md_text.lower().startswith('внимание, анекдот'), 
                    content_types='photo',
                    user_id = USER_ID)
async def sarcastic_reply(message):
    await message.reply(random.choice(answer_var))

@dp.message_handler(content_types='photo',
                    user_id = USER_ID)
async def not_funny_picture(message):
    await message.reply('Не уверен, что это значит, но очень смешно')

@dp.message_handler(commands=['status'])
async def get_status(message):
    await message.reply('Я НЕ СПЛЮ')

async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_URL)

async def on_shutdown(dp):
    logging.warning('Shutting down...')
    await bot.delete_webhook()
    logging.warning('Bye!')
    
if __name__=="__main__":
    executor.start_polling(dp, skip_updates=True)
