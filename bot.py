from aiogram import Bot, Dispatcher, executor
import os
import random
import logging

API_TOKEN = os.getenv('API_TOKEN')
USER_ID = os.getenv('USER_ID')

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

if __name__=="__main__":
    executor.start_polling(dp, skip_updates=True)
