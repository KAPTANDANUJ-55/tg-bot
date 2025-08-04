from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, CallbackQueryHandler

async def menu(update, context):
    keyboard = [
        [InlineKeyboardButton("🔥 Masti", callback_data='masti')],
        [InlineKeyboardButton("📚 Gyaan", callback_data='gyaan')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Kya chahiye bhai? Choose:", reply_markup=reply_markup)

async def handle_buttons(update, context):
    query = update.callback_query
    await query.answer()

    if query.data == 'masti':
        await query.edit_message_text("Masti mode on! 😎")
    elif query.data == 'gyaan':
        await query.edit_message_text("Gyaan time, padho beta! 📖")

button_command_handler = CommandHandler("menu", menu)
button_callback_handler = CallbackQueryHandler(handle_buttons)
