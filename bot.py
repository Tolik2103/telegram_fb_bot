from telegram.ext import Updater, MessageHandler, Filters

# 🔐 Твій токен від BotFather
TELEGRAM_TOKEN = '8327688810:AAEcuzr4ailCGtBThC58CEwZWWJc7Th2Ct8'

# 🔧 Обробка постів у каналі
def handle_channel_post(update, context):
    post = update.channel_post
    if post:
        chat_id = post.chat.id
        text = post.text if post.text else "[немає тексту]"
        print(f"📢 Пост у каналі: {text}")
        print(f"🆔 Chat ID каналу: {chat_id}")

# 🚀 Запуск бота
def main():
    updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Додаємо обробник для channel_post
    dispatcher.add_handler(MessageHandler(Filters.update.channel_posts, handle_channel_post))

    print("✅ Бот запущено. Очікування постів у каналі...")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
