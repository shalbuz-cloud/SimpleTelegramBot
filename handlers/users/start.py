from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from utils.set_bot_commands import set_starting_commands


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer('Привет, %s!' % message.from_user.full_name)
    await set_starting_commands(message.bot, message.from_user.id)
