from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os
from dotenv import load_dotenv


load_dotenv()

storage = MemoryStorage()

bot = Bot(token=os.getenv('token'))
dp = Dispatcher(bot, storage=storage)
