from telegram.ext import Updater, MessageHandler, Filters

TELEGRAM_TOKEN = '8327688810:AAEcuzr4ailCGtBThC58CEwZWWJc7Th2Ct8'

def handle_message(update, context):
    message = update.message
    if message and message.text:
        print(f"Нове повідомлення: {message.text}")

updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

print("Бот запущено. Очікування повідомлень у групі...")
updater.start_polling()
updater.idle()
