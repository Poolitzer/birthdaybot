import datetime
import html

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ChatAction, ChatMember
from telegram.ext import CallbackContext
from strings import (INTRO, BIRTHDAY_FAIL, SAY_NAME, LINK, LINK_APPROVED, LINK_DECLINED, BIRTHDAY_SHOW, FINAL, FALLBACK,
                     NOT_IN_GROUP, YES, NO)
from json_handler import save_birthdays
from telegraph_handler import update_page
from birthday_celebration import set_birthday
from hardcode_values import GROUP_ID

BIRTHDAY, NAME, USERNAME, SHOW_BIRTHDAY = range(4)


def init_birthday(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    if member := context.bot.get_chat_member(GROUP_ID, user_id):
        if member.status in [ChatMember.KICKED, ChatMember.LEFT, ChatMember.RESTRICTED]:
            update.effective_message.reply_text(NOT_IN_GROUP)
            return -1
        update.effective_message.reply_text(INTRO)
        return BIRTHDAY
    else:
        update.effective_message.reply_text(NOT_IN_GROUP)
        return -1


def ask_name(update: Update, context: CallbackContext):
    message = update.effective_message
    text = message.text
    try:
        birthday = datetime.datetime.strptime(text, "%d.%m.%Y")
    except ValueError:
        message.reply_text(BIRTHDAY_FAIL)
        return
    age = _calculate_age2(birthday)
    context.user_data.update({"birthday": text, "age": age})
    message.reply_text(SAY_NAME)
    return NAME


def _create_inlinekeyboard():
    buttons = [[InlineKeyboardButton(YES, callback_data="y"), InlineKeyboardButton(NO, callback_data="n")]]
    return InlineKeyboardMarkup(buttons)


def after_name(update: Update, context: CallbackContext):
    message = update.effective_message
    context.user_data["name"] = html.escape(message.text)
    buttons = _create_inlinekeyboard()
    if update.effective_user.username:
        message.reply_text(LINK, reply_markup=buttons)
        return USERNAME
    else:
        message.reply_text(BIRTHDAY_SHOW, reply_markup=buttons)
        return SHOW_BIRTHDAY


def link(update: Update, context: CallbackContext):
    query = update.callback_query
    buttons = _create_inlinekeyboard()
    query.answer()
    if query.data == "y":
        context.user_data["link"] = update.effective_user.link
        query.edit_message_text(LINK_APPROVED + BIRTHDAY_SHOW, reply_markup=buttons)
    else:
        context.user_data["link"] = ""
        query.edit_message_text(LINK_DECLINED + BIRTHDAY_SHOW, reply_markup=buttons)
    return SHOW_BIRTHDAY


# https://stackoverflow.com/a/30815748
def _calculate_age2(birthdate):
    today = datetime.date.today()
    this_year_birthday = datetime.date(today.year, birthdate.month, birthdate.day)
    if this_year_birthday < today:
        years = today.year - birthdate.year
    else:
        years = today.year - birthdate.year - 1
    return years


def show_birthday(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    user_data = context.user_data
    dewit = False
    if query.data == "y":
        dewit = True
    birthday = {str(update.effective_user.id): {"name": user_data["name"], "birthday": user_data["birthday"],
                                                "age": user_data["age"], "link": user_data["link"],
                                                "show_birthday": dewit}}
    user_data.clear()
    save_birthdays(birthday)
    update_page()
    set_birthday(context.job_queue)
    query.edit_message_text(FINAL)
    # -1 is ending the conversationhandler
    return -1


def cancel(update: Update, context: CallbackContext):
    context.user_data.clear()
    update.effective_message.reply_text(FALLBACK)
    # -1 is ending the conversationhandler
    return -1
