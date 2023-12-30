import os
import json
import requests
import time
from CTA import CTA


def build_message():
    set_timezone()
    bus_data = CTA(os.environ["cta_bus_api_key"],
                   os.environ["notify_stpid"].split(","),
                   "",
                   os.environ["notify_rt"].split(","),
                   log=True).get_data()
    msg = "Upcoming %s buses @ %s:\n" % (os.environ["notify_rt"],  os.environ["notify_stop_name"]) if len(bus_data) > 0 \
        else "No upcoming buses\n"
    for bus in bus_data:
        prdtm = bus['prdtm'].split(" ")[1]
        hour = prdtm.split(":")[0]
        minute = prdtm.split(":")[1]
        msg += "\t- %s:%s %s (%s min)\n" % (int(hour) % 12, minute, "am" if int(hour) < 12 else "pm", bus['prdctdn'])

    return msg


def post_to_slack(msg):
    return requests.post(os.environ['slack_webhook'], json={'text': msg})


def lambda_handler(event, context):
    post_to_slack(build_message())

    return


def load_secrets(secret_names):
    # Load secrets (that would otherwise be set in the aws configuration)
    f = open("../overlays/secrets.json")
    secrets = json.load(f)
    f.close()
    for name in secret_names:
        os.environ[name] = secrets[name]


def set_timezone():
    os.environ['TZ'] = 'US/Central'
    time.tzset()


if __name__ == "__main__":
    secret_names = ["slack_webhook", "cta_bus_api_key", "notify_rt", "notify_stop_name", "notify_stpid"]
    load_secrets(secret_names)
    print(build_message())
