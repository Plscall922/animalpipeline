import logging
import sys
from apscheduler.schedulers.blocking import BlockingScheduler
from telegramfactory.animalbot.telegram_animal_bot import post_to_telegram, start_command_listener
from pytz import timezone

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
)

def schedule_bot():
    scheduler = BlockingScheduler()
    scheduler.add_job(post_to_telegram, 'cron', hour=12, minute=0, timezone=timezone('Australia/Sydney'))
    logging.info("Scheduler started. Will post every Mon/Wed/Fri at 12:00 PM.")
    scheduler.start()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "test":
            logging.info("Running manual test post...")
            post_to_telegram()
        elif sys.argv[1] == "listen":
            start_command_listener()
    else:
        schedule_bot()
