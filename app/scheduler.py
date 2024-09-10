from apscheduler.schedulers.background import BackgroundScheduler
from app.garak import run_garak_scan

scheduler = BackgroundScheduler()

def schedule_scan(endpoint, interval):
    # Schedule a scan to run every 'interval' minutes
    scheduler.add_job(lambda: run_garak_scan(endpoint), 'interval', minutes=interval)
    scheduler.start()
