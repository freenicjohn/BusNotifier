import os
import requests
import time
from CTA import CTA
from dotenv import load_dotenv


from datetime import datetime


def log(message):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"{timestamp} | {message}")


def build_message():
    set_timezone()
    log("Fetching CTA bus data...")
    bus_data = CTA(
        os.getenv("CTA_BUS_API_KEY"),
        os.getenv("NOTIFY_STPID").split(","),
        "",
        os.getenv("NOTIFY_RT").split(","),
        log=True
    ).get_data()
    if bus_data and len(bus_data) > 0:
        msg = "Upcoming %s buses @ %s:\n" % (os.getenv("NOTIFY_RT"), os.getenv("NOTIFY_STOP_NAME"))
    else:
        msg = "No upcoming buses\n"
    for bus in bus_data or []:
        prdtm = bus['prdtm'].split(" ")[1]
        hour = prdtm.split(":")[0]
        minute = prdtm.split(":")[1]
        msg += "\t- %s:%s %s (%s min)\n" % (int(hour) % 12, minute, "am" if int(hour) < 12 else "pm", bus['prdctdn'])
    return msg


def post_to_slack(msg):
    log("Posting message to Slack...")
    return requests.post(os.getenv('BUS_SLACK_WEBHOOK'), json={'text': msg})


def set_timezone():
    os.environ['TZ'] = 'US/Central'
    time.tzset()


if __name__ == "__main__":
    load_dotenv()
    set_timezone()
    log("Starting BusNotifier...")
    post_to_slack(build_message())
    log("Done.")
