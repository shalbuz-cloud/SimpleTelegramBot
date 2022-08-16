from aiogram import types, Bot
from aiogram import Dispatcher
from aiogram.types import (BotCommandScopeDefault, BotCommandScopeChat,
                           BotCommandScopeAllGroupChats,
                           BotCommandScopeAllPrivateChats,
                           BotCommandScopeAllChatAdministrators, BotCommand,
                           BotCommandScopeChatAdministrators,
                           BotCommandScopeChatMember)


async def set_default_commands(dp: Dispatcher):
    await dp.bot.set_my_commands(
        [
            types.BotCommand('start', 'Запустить бота'),
            types.BotCommand('help', 'Вывести справку'),
        ],
        # scope=BotCommandScopeDefault(),
    )


async def set_starting_commands(bot: Bot, chat_id: int):
    """Команды после запуска бота"""
    STARTING_COMMANDS = {
        'ru': [
            types.BotCommand('start', 'Начать заново'),
            types.BotCommand('get_commands', 'Получить список команд'),
            types.BotCommand('reset_commands', 'Сбросить команды'),
        ],
        'en': [
            types.BotCommand('start', 'Restart bot'),
            types.BotCommand('get_commands', 'Retrieve command list'),
            types.BotCommand('reset_commands', 'Reset commands')
        ]
    }
    for language_code, commands in STARTING_COMMANDS.items():
        await bot.set_my_commands(
            commands=commands,
            scope=BotCommandScopeChat(chat_id),
            language_code=language_code
        )


async def force_reset_all_commands(dp: Dispatcher):
    for language_code in ('ru', 'en', 'uk', 'uz'):
        for scope in (
                BotCommandScopeAllGroupChats(),
                BotCommandScopeAllPrivateChats(),
                BotCommandScopeAllChatAdministrators(),
                BotCommandScopeDefault()
        ):
            await dp.bot.delete_my_commands(scope, language_code)


async def set_all_group_commands(bot: Bot):
    """Команды для пользователей"""
    return await bot.set_my_commands(
        commands=[
            BotCommand('start', 'Информация о боте'),
            BotCommand('report', 'Пожаловаться на пользователя'),
        ],
        scope=BotCommandScopeAllGroupChats()
    )


async def set_all_chat_admins_commands(bot: Bot):
    """Команды администраторов"""
    return await bot.set_my_commands(
        commands=[
            BotCommand('ro', 'Мут пользователя'),
            BotCommand('ban', 'Бан пользователя'),
            BotCommand('change_commands', 'Изменить команды в этом чате')
        ],
        scope=BotCommandScopeAllChatAdministrators()
    )


async def set_chat_admins_commands(bot: Bot, chat_id: int):
    """Для администраторов определенного группового чата"""
    return await bot.set_my_commands(
        commands=[
            BotCommand('ro', 'Мут пользователя'),
            BotCommand('ban', 'Забанить пользователя'),
            BotCommand('reset_commands', 'Сбросить команды'),
        ],
        scope=BotCommandScopeChatAdministrators(chat_id)
    )


async def set_chat_member_commands(bot: Bot, chat_id, user_id):
    """Установка прав участника чата"""
    return await bot.set_my_commands(
        commands=[BotCommand('promote', 'Повысить до админа')],
        scope=BotCommandScopeChatMember(chat_id, user_id)
    )


async def set_all_private_commands(bot: Bot):
    return await bot.set_my_commands(
        commands=[
            BotCommand('account', 'Настройки аккаунта'),
            BotCommand('wallet', 'Кошелек'),
            BotCommand('reset_commands', 'Сбросить команды'),
        ],
        scope=BotCommandScopeAllPrivateChats()
    )
