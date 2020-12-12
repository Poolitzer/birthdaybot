import datetime
from random import choice

from telegram.ext import JobQueue, CallbackContext
from telegram.utils.helpers import mention_html

from hardcode_values import GROUP_ID, TIME
from strings import GRATULATIONS
import json_handler
from telegraph_handler import update_page


def _next_job(job_queue: JobQueue, birthday_id, birthday):
    job_queue.run_daily(celebrate_birthday, TIME, name=birthday_id,
                        context={"birthday": birthday["birthday"], "name": birthday["name"], "age": birthday["age"]})


def celebrate_birthday(context: CallbackContext):
    job = context.job
    data = job.context
    birthday_id = job.name
    birthday = datetime.datetime.strptime(data["birthday"], "%d.%m.%Y")
    today = datetime.datetime.now()
    if [today.day, today.month] != [birthday.day, birthday.month]:
        return
    json_handler.increase_age(birthday_id)
    context.bot.send_message(GROUP_ID, choice(GRATULATIONS).format(mention_html(int(birthday_id), data["name"]),
                                                                   data["age"] + 1), parse_mode="HTML")
    birthday = json_handler.next_birthday(context.job_queue)
    job.name = birthday[0]
    job.context = {"birthday": birthday[1]["birthday"], "name": birthday[1]["name"], "age": birthday[1]["age"]}
    update_page()


# used when starting the bot or entering a new birthday
def set_birthday(job_queue: JobQueue):
    birthday = json_handler.next_birthday(job_queue)
    if not birthday:
        # no birthday in the file, no need to set the job
        return
    birthday_id = birthday[0]
    jobs = job_queue.jobs()
    # only the job with an integer as a name is the birthday job. Now we can do more jobs, unrelated to birthdays,
    # if we want to.
    wanted_job = [job for job in jobs if type(job.name) == int]
    # making sure we actually have a jobqueue
    if wanted_job:
        # next birthday is the one in our jobqueue, we are good to go
        if wanted_job[0].name == birthday_id:
            return
        # next birthday is a new one, lets end the old and start a new
        wanted_job[0].schedule_removal()
    _next_job(job_queue, birthday_id, birthday[1])
