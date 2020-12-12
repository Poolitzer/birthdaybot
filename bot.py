from telegram.ext import Updater, ConversationHandler, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from birthday_celebration import set_birthday
import add_birthday_handler
import logging

from hardcode_values import TELEGRAM_TOKEN

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO, filename="log.log")
aps_logger = logging.getLogger('apscheduler')
aps_logger.setLevel(logging.WARNING)


def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", add_birthday_handler.init_birthday, Filters.chat_type.private)],
        states={
            add_birthday_handler.BIRTHDAY: [MessageHandler(Filters.text & ~Filters.command,
                                                           add_birthday_handler.ask_name)],
            add_birthday_handler.NAME: [MessageHandler(Filters.text & ~Filters.command,
                                                       add_birthday_handler.after_name)],
            add_birthday_handler.USERNAME: [CallbackQueryHandler(add_birthday_handler.link)],
            add_birthday_handler.SHOW_BIRTHDAY: [CallbackQueryHandler(add_birthday_handler.show_birthday)]
        },
        fallbacks=[CommandHandler("cancel", add_birthday_handler.cancel)]
    )
    dp.add_handler(conv_handler)
    updater.start_polling()
    # we have to add the next birthday to our jobqueue
    set_birthday(updater.job_queue)
    updater.idle()


if __name__ == '__main__':
    main()
