import logging
from apscheduler.schedulers.blocking import BlockingScheduler
from animalpipeline.telegramfactory.animalbot.telegram_animal_bot import post_to_telegram

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
)

def schedule_bot():
    scheduler = BlockingScheduler()
    scheduler.add_job(post_to_telegram, 'cron', day_of_week='mon,wed,fri', hour=12, minute=0)
    logging.info("Scheduler started. Will post every Mon/Wed/Fri at 12:00 PM.")
    scheduler.start()

if __name__ == "__main__":
    schedule_bot()