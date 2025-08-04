from telegram.ext import CommandHandler

async def send_photo(update, context):
    await update.message.reply_photo(
        photo="https://i.imgur.com/VWuYDQ1.jpg",
        caption="TERI PETI PACK PHOTO"
    )

image_handler = CommandHandler("photo", send_photo)
