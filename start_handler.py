from telegram.ext import CommandHandler

async def start(update, context):
    await update.message.reply_text("Yo Danuj bhai! Bot activated! 🔥")

start_handler = CommandHandler("start", start)
