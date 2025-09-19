from telegram.ext import Updater, MessageHandler, Filters

TELEGRAM_TOKEN = 8327688810:AAEcuzr4ailCGtBThC58CEwZWWJc7Th2Ct8

def handle_channel_post(update, context):
    post = update.channel_post
    if post and post.text:
        print(f"Пост у каналі: {post.text}")

updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Обробник для постів у каналі
dispatcher.add_handler(MessageHandler(Filters.update.channel_posts, handle_channel_post))

print("Бот запущено. Очікування постів у каналі...")
updater.start_polling()
updater.idle()