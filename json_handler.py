import json
from datetime import datetime
from random import choice
from functools import partial

from hardcode_values import GROUP_ID
from strings import GRATULATIONS
from telegram.ext import JobQueue
from telegram.utils.helpers import mention_html

_dates = json.load(open("birthdays.json"))


def save_birthdays(new_birthday):
    _dates.update(new_birthday)
    with open('birthdays.json', 'w') as outfile:
        json.dump(_dates, outfile, indent=4, sort_keys=True)


def return_birthdays():
    birthdays = []
    for birthday_id in _dates:
        birthdays.append(_dates[birthday_id])
    return birthdays


def _seconds(date, against):
    delta = date[1] - against
    delta_seconds = delta.total_seconds()
    if delta_seconds == 0:
        return -0.1
    return -1 / delta_seconds


def next_birthday(job_queue: JobQueue):
    from telegraph_handler import update_page
    birthdays = []
    for birthday_id in _dates:
        birthdays.append([birthday_id, datetime.strptime(_dates[birthday_id]["birthday"][:-5], "%d.%m")])
    today = datetime.now()
    against = datetime(year=1900, month=today.month, day=today.day)
    birthdays_sorted = sorted(birthdays, key=partial(_seconds, against=against))
    closest_birthday_id = 0
    for birthday in birthdays_sorted:
        birthdate = birthday[1].date()
        # this means birthday is today
        if [birthdate.day, birthdate.month] == [today.day, today.month]:
            if today.year - int(_dates[birthday[0]]["birthday"][-4:]) - _dates[birthday[0]]["age"]:
                # this means we have to celebrate (since the difference isnt 0), so lets do this
                increase_age(birthday[0])
                msg = choice(GRATULATIONS).format(mention_html(int(birthday[0]), _dates[birthday[0]]["name"]),
                                                  _dates[birthday[0]]["age"])
                job_queue._dispatcher.bot.send_message(GROUP_ID, msg, parse_mode="HTML")
                update_page()
                continue
        closest_birthday_id = birthday[0]
        break
    if closest_birthday_id == 0:
        # two situations can lead us here: the only birthday has birthday today or there are no birthdays in the file
        # yet. Lets handle both
        if _dates:
            only_id = list(_dates.keys())[0]
            return [only_id, _dates[only_id]]
        return False
    return [closest_birthday_id, _dates[closest_birthday_id]]


def increase_age(birthday_id):
    new_age = _dates[birthday_id]["age"]
    new_age += 1
    _dates[birthday_id].update({"age": new_age})
    with open('birthdays.json', 'w') as outfile:
        json.dump(_dates, outfile, indent=4, sort_keys=True)
