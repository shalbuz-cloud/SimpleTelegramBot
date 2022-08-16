from aiogram import Dispatcher
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, BotCommandScopeChat, ChatType
from aiogram.utils.markdown import quote_html

from loader import dp
from utils.set_bot_commands import set_chat_admins_commands


@dp.message_handler(Command('get_commands'))
async def message_get_command(message: Message):
    no_lang = await message.bot.get_my_commands(
        scope=BotCommandScopeChat(message.from_user.id)
    )
    no_args = await message.bot.get_my_commands()
    ru_lang = await message.bot.get_my_commands(
        scope=BotCommandScopeChat(message.from_user.id),
        language_code='ru'
    )
    # quote_html - для экранирования символов. Из-за назначенного
    # глобально parse_mode='HTML'. Иначе может приводить к ошибкам,
    # при выводе объектов Python
    await message.reply('\n\n'.join(
        # 'arg=%(arg)s' % {'arg': i for i in (no_args, no_lang, ru_lang)}
        # f"{arg=}" for arg in (no_args, no_lang, ru_lang)
        f"<pre>{quote_html(arg)}</>" for arg in (no_args, no_lang, ru_lang)
    ))


@dp.message_handler(Command('reset_commands'))
async def message_reset_commands(message: Message):
    await message.bot.delete_my_commands(
        BotCommandScopeChat(message.from_user.id),
        language_code='en'
    )
    await message.reply('Команды были удалены')


@dp.message_handler(Command('change_commands'))
async def change_admin_commands(message: Message):
    await set_chat_admins_commands(message.bot, message.chat.id)
    await message.answer(
        'Команды администраторов для этого чата были изменены'
    )
