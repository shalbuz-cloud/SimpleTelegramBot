from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.dispatcher.filters import Command, Text

from loader import dp
from keyboards.default import menu


@dp.message_handler(Command('menu'))
async def show_menu(message: Message):
    await message.answer('Выберите товар из меню ниже', reply_markup=menu)


@dp.message_handler(Text(equals=['Котлетки', 'Макарошки', 'Пюрешка']))
# Вариант 2 - @dp.message_handler(text='Пюрешка')
# Вариант 3 - @dp.message_handler(Text(equals='Пюрешка'))
async def get_food(message: Message):
    await message.answer(
        'Вы выбрали %s. Спасибо' % message.text,
        reply_markup=ReplyKeyboardRemove()  # Убираем кнопки
    )
