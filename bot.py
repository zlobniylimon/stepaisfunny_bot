from aiogram import Bot, Dispatcher, executor
import os
import random
import logging
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')
USER_ID = os.getenv('USER_ID')

IP_HOST = os.getenv('HOST')
WEBHOOK_HOST = f'https://{IP_HOST}'
WEBHOOK_PATH = f'/webhook/{API_TOKEN}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = int(os.getenv('PORT'))

logging.basicConfig(level=logging.INFO)

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

@dp.message_handler(lambda message: message.text.lower().startswith('внимание, анекдот'))
async def sarcastic_reply(message):
    if message.from_user.id == int(USER_ID):
        await message.reply(random.choice(answer_var))

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
    executor.start_webhook(
            dispatcher=dp,
            webhook_path=WEBHOOK_PATH,
            on_startup=on_startup,
            on_shutdown=on_shutdown,
            skip_updates=True,
            host=WEBAPP_HOST,
            port=WEBAPP_PORT,
            )

