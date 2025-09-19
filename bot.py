from telegram import Bot

TELEGRAM_TOKEN = "8327688810:AAEcuzr4ailCGtBThC58CEwZWWJc7Th2Ct8"
CHANNEL_ID = '@TamashiinoHikari'

bot = Bot(token=TELEGRAM_TOKEN)
bot.send_message(chat_id=CHANNEL_ID, text='Привіт! Це тестовий пост у канал.')
print("✅ Повідомлення надіслано.")
