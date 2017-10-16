# Global Entry Interview Openings Checker

This script uses the new (2017-10) but undocumented API at `https://ttp.cbp.dhs.gov/schedulerapi/slots/asLocations` to inform you of Global Entry interview openings.

## Setup

- If you don't have a Twilio account, [create one]() for free, and create a free [phone number](https://www.twilio.com/console/phone-numbers). This is where your texts will originate from.
- Install the dependencies `pip install -r requirements.txt`
- Copy `config.py.template` to a new file `config.py`
- Edit `config.py`:
  - Enter your Twilio [tokens](https://www.twilio.com/console)
  - Enter your Twilio ['from' phone number](https://www.twilio.com/console/phone-numbers)  - - Enter your desired destination cell number, amount of weeks to look ahead, and your city search string.
- add this script to your crontab (see [virtualenv notes](https://stackoverflow.com/questions/3287038/cron-and-virtualenv))
- wait for it