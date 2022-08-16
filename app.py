from aiogram import executor, Dispatcher

from loader import dp
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import (set_default_commands,
                                    set_all_group_commands,
                                    set_all_chat_admins_commands,
                                    set_all_private_commands)


async def on_startup(dispatcher: Dispatcher):
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)
    await set_all_group_commands(dispatcher.bot)
    await set_all_chat_admins_commands(dispatcher.bot)
    await set_all_private_commands(dispatcher.bot)
    # Уведомляет про запуск
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
