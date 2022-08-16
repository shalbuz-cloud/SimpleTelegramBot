import logging

from aiogram.utils.exceptions import (TelegramAPIError, MessageNotModified,
                                      CantParseEntities)

from loader import dp


@dp.errors_handler()
async def errors_handler(update, exception):
    """
    Exceptions handler. Catches all exceptions within task factory tasks.
    :param update:
    :param exception:
    :return: stdout logging
    """

    if isinstance(exception, MessageNotModified):
        logging.exception('Message not modified')
        # do something here?
        return True

    if isinstance(exception, CantParseEntities):
        # or here
        logging.exception(
            'CantParseEntities: %s \nUpdate: %s' % (exception, update)
        )
        return True

    # MUST BE THE LAST CONDITION
    if isinstance(exception, TelegramAPIError):
        logging.exception(
            'TelegramAPIError: %s\nUpdate: %s' % (exception, update)
        )
        return True

    # At least you have tried.
    logging.exception('Update: %s\n%s' % update, exception)
