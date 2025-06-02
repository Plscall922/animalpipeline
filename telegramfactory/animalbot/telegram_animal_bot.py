import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import os
import logging
import asyncio
from dotenv import load_dotenv
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, ContextTypes
from openaigenerator.animalfacts.impl import generate_cute_post

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# Async post generator
async def post_to_telegram_async():
    result = generate_cute_post()
    if result:
        animal, text = result
        try:
            bot = Bot(token=TOKEN)
            await bot.send_message(
                chat_id=CHAT_ID,
                text=f"🐾 {animal.capitalize()} says:\n\n{text}"
            )
            logging.info("Posted to Telegram.")
        except Exception as e:
            logging.error(f"Telegram send failed: {e}")
    else:
        logging.warning("No content generated.")

# Manual trigger via /test command
async def handle_test(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await post_to_telegram_async()
    await update.message.reply_text("✅ Cute animal post triggered!")

# Manual run (optional utility)
def post_to_telegram():
    asyncio.run(post_to_telegram_async())

def start_command_listener():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("test", handle_test))
    logging.info("Telegram command listener started.")
    app.run_polling()
