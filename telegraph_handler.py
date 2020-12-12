import json
import requests
import logging

from hardcode_values import TELEGRAPH_TOKEN, ARTICLE_ID, TELEGRAPH_TITLE
from strings import YEARS
from json_handler import return_birthdays

logger = logging.getLogger(__name__)


def _content_generator(birthdays):
    content = [{'tag': 'ul', 'children': []}]
    content_to_update = content[0]["children"]
    for birthday in birthdays:
        if birthday["link"]:
            name = {'tag': 'a', 'attrs': {'href': f'{birthday["link"]}'}, 'children': [birthday["name"]]}
        else:
            name = birthday["name"]
        years = f": {birthday['age']} {YEARS}"
        if birthday["show_birthday"]:
            # turn our next_celeberation_date in actual birthdate
            years += f" – {birthday['birthday']}"
        bullet_point = {'tag': 'li', 'children': [name, years]}
        content_to_update.append(bullet_point)
    return content


def update_page():
    content = _content_generator(return_birthdays())
    stuff = {"access_token": TELEGRAPH_TOKEN,
             "title": TELEGRAPH_TITLE, "content": json.dumps(content), "return_content": True}
    r = requests.post("https://api.telegra.ph/editPage/" + ARTICLE_ID, data=stuff)
    if r.status_code == 200:
        if r.json()["ok"]:
            pass
        else:
            logger.error(f"Telegraph returned a false error: {r.json()}")
    else:
        logger.error(f"Telegraph returned a non 200 code: {r.status_code} + {r.content}")
