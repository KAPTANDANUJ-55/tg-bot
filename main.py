from telegram.ext import ApplicationBuilder
from handlers.start_handler import start_handler
from handlers.image_handler import image_handler
from handlers.button_handler import button_command_handler, button_callback_handler
from utils.logger import setup_logger
import asyncio

async def main():
    setup_logger()

    app = ApplicationBuilder().token("").build()

    # Add all handlers
    app.add_handler(start_handler)
    app.add_handler(image_handler)
    app.add_handler(button_command_handler)
    app.add_handler(button_callback_handler)

    print("Bot is running...")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
