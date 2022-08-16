from aiogram.dispatcher.filters.state import StatesGroup, State


class Test(StatesGroup):
    """
    Создаем тест с помощью машины состояний.
    Создаем класс фильтров состояний, который наследует объект
    группы состояний StatesGroup.
    Отдельное состояние - фильтр State. Порядок имеет значение.
    """
    Q1 = State()
    Q2 = State()
