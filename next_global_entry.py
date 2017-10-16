#!/bin/env python
"""Check for Global Entry interview openings in your city."""

import sys
import datetime
import requests
from twilio.rest import Client
import config

if __name__ == '__main__':
    # calculate date
    now = datetime.datetime.now()
    delta = datetime.timedelta(weeks=config.look_ahead_weeks)
    future = now + delta
    request_url = config.global_entry_query_url.format(
        timestamp=future.strftime("%Y-%m-%d"))
    print(request_url)
    result = requests.get(request_url).json()
    cities = [o.get('city').lower() for o in result]
    if config.search_string.lower() in cities:
        client = Client(config.twilio_account, config.twilio_token)
        message = client.messages.create(
            to=config.to_number,
            from_=config.twilio_from_number,
            body="Global Entry interview opportunity in {} \
opened up just now!".format(config.search_string))
        sys.exit(0)
    sys.exit(1)
