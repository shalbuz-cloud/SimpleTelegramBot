from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            # Первая строка
            KeyboardButton(text='Котлетки'),
        ],
        [
            # Вторая строка
            KeyboardButton(text='Макарошки'),
            KeyboardButton(text='Пюрешка')
        ],
    ],
    resize_keyboard=True
)
