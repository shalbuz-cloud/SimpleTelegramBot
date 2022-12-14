import logging

from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from keyboards.inline.callback_data import buy_callback
from loader import dp
from keyboards.inline.choice_buttons import (choice, pear_keyboard,
                                             apples_keyboard)


@dp.message_handler(Command('items'))
async def show_items(message: Message):
    await message.answer(text='На продажу у нас есть 2 товара: 5 Яблок и'
                              ' 1 Груша.\n'
                              'Если вам ничего не нужно - жмите отмену',
                         reply_markup=choice)


@dp.callback_query_handler(buy_callback.filter(item_name='apple'))
async def buying_apples(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info('call = %s' % callback_data)
    quantity = callback_data.get('quantity')
    await call.message.answer(
        'Вы выбрали купить яблоки. Яблок всего %s. Спасибо.' % quantity,
        reply_markup=apples_keyboard
    )


@dp.callback_query_handler(text_contains='pear')
# text_contains - все нажатия с совпадением "pear"
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info('call = %s' % callback_data)

    await call.message.answer(
        'Вы выбрали купить грушу. Груша всего одна. Спасибо.',
        reply_markup=pear_keyboard
    )


@dp.callback_query_handler(text='cancel')
async def cancel_buying(call: CallbackQuery):
    await call.answer('Вы отменили эту покупку!', show_alert=True)
    await call.message.edit_reply_markup()
