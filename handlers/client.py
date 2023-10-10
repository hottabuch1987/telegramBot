from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client, kb_url_client
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db


async def command_start(message : types.message):
    try:
        await bot.send_message(message.from_user.id, 'Добро пожаловать в мой магазин', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/my_bot_arikbot')


async def open_command(message : types.message):
    try:
        await bot.send_message(message.from_user.id, 'Вс-Чт с 9:00 до 20:00, Пт-Сб с 10:00 до 23:00')
    except:
        await message.reply('Попробуйте еще раз, произошла ошибка')


async def place_command(message : types.message): 
    try:
        await bot.send_message(message.from_user.id, 'г.Армавир ул. Ленина 110')
    except:
        await message.reply('Попробуйте еще раз, произошла ошибка')

async def exit_command(message : types.message): 
    try:
        await bot.send_message(message.from_user.id, 'я буду скучать', reply_markup=ReplyKeyboardRemove())
    except:
        await message.reply('Попробуйте еще раз, произошла ошибка')

async def catalog_command(message : types.message): 
    await sqlite_db.sql_reload(message)




async def url_command(message : types.Message):
    await message.reply('ссылки', reply_markup=kb_url_client)

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(open_command, commands=['режим_работы'])
    dp.register_message_handler(place_command, commands=['расположение'])
    dp.register_message_handler(exit_command, commands=['выйти'])
    dp.register_message_handler(catalog_command, commands=['каталог'])
    dp.register_message_handler(url_command, commands=['ссылки'])
    
