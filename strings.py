from hardcode_values import GROUP_NAME, TELEGRAPH_TITLE


INTRO = "Hey you. You want to be in the birthday list of our group? Great. Please tell me your birthday. " \
        "I expect the format DD.MM.YYYY"
BIRTHDAY_FAIL = "Amazing. Your birthday is ******..... Beep buup.... Converting input to birthday " \
                "failed.\n\nPlese send your birthday in the format DD.MM.YYYY or use /cancel"
SAY_NAME = "Great, I saved your birthday. With which name do you want to appear on the list?"
LINK = "I see that you have an username. Do you want your name on the list to be linked to your telegram profile?"
# we need the spaces after the dots because we combine it with Birthday_Show
LINK_APPROVED = "Okay, I am going to link your name to your username. "
LINK_DECLINED = "Okay, I am not going to link your name. "
BIRTHDAY_SHOW = "Do you want to have your birthday appear next to your name on the list?"
FINAL = "Alright, thanks. I saved your data and updated the telegraph article. Have a good day."
GRATULATIONS = ["{0}, happy birthday. You are {1} now!",
                "It is {0}'s birthday today, 🎉. {1} years old.", "GUYS. GIRLS. {0}. BIRTHDAY. {1}. YEARS.",
                "Congratulation, {0}, it is your birthday, {1} years already, holy cow.",
                "Who can remember the time when they were {1} years old?{0} definitely can, they are that today \\o/",
                "{0} managed to have birthday today and is {1} years old.",
                "🎊🎉🥳🥳🥳🥳🙌🎉🎉🎉{0}🎊🎉🎊🎉🎊🎉🥳🙌🎉🥳🙌🎉🥳🙌🎉🥳🙌🎉{1}"]
FALLBACK = "Abort. ABORT. You did not make it on the list :("
NOT_IN_GROUP = f"Hey, you are not in the great {GROUP_NAME} chat, I can't add you this way :("
YES = "Yes"
NO = "No"
YEARS = "years"
