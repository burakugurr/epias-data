import schedule
import time
import requests

def run_api():
    requests.get('http://localhost:8000/market/mcp')


schedule.every().day.at("16:00").do(run_api)

while True:
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)