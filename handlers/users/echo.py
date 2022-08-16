from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp


# # Эхо хендлер, куда летят текстовые сообщения без указанного состояния
# @dp.message_handler(state=None)
# async def bot_echo(message: types.Message):
#     await message.answer('Эхо без состояния.\n'
#                          'Сообщение:\n%s' % message.text)


# Эхо хендлер, куда летят все сообщения с указанным состоянием
@dp.message_handler(state='*', content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    state = await state.get_state()
    await message.answer('Эхо в состоянии <code>%s<code>.\n'
                         '\nСодержание сообщения:\n'
                         '<code>%s<code>' % (state, message))
