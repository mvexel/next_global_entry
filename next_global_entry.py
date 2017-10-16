#!/usr/bin/env python
"""Check for Global Entry interview openings in your city."""

import sys
import datetime
import requests
from twilio.rest import Client
import config


def log(text):
    """Write a one-line log message."""
    print("{dt}\t{msg}".format(
        dt=datetime.datetime.now(),
        msg=text))


if __name__ == '__main__':
    # calculate date
    now = datetime.datetime.now()
    delta = datetime.timedelta(weeks=config.look_ahead_weeks)
    future = now + delta
    request_url = config.global_entry_query_url.format(
        timestamp=future.strftime("%Y-%m-%d"))
    result = requests.get(request_url).json()
    cities = [o.get('city').lower() for o in result]
    if config.search_string.lower() in cities:
        client = Client(config.twilio_account, config.twilio_token)
        message = client.messages.create(
            to=config.to_number,
            from_=config.twilio_from_number,
            body="Global Entry interview opportunity in {} \
opened up just now!".format(config.search_string))
        log("text message sent")
        sys.exit(0)
    log("no news")
    sys.exit(1)
