import os
import logging
from dotenv import load_dotenv
from telegram import Bot
from telegram.error import TelegramError
from animalpipeline.openaigenerator.animalfacts.impl import generate_cute_post

load_dotenv()
telegram_token = os.getenv("TELEGRAM_BOT_TOKEN")
chat_id = os.getenv("TELEGRAM_CHAT_ID")
telegram_bot = Bot(token=telegram_token)

def post_to_telegram():
    result = generate_cute_post()
    if result:
        animal, text = result
        try:
            telegram_bot.send_message(chat_id=chat_id, text=f"🐾 {animal.capitalize()} says:\n\n{text}")
            logging.info("Posted to Telegram.")
        except TelegramError as e:
            logging.error(f"Telegram post failed: {e}")
    else:
        logging.warning("No content generated, skipping Telegram post.")
