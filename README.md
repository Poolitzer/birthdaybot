The Birthday Bot.

This is a simple telegram bot I wrote a while ago to manage the birthdays in a group I am a member in. Accordingly focused is the bot and it requires a bit of setting up.

It takes the birthdays of members when they PM the bot (and ask not members to join the group). Then it updates a telegra.ph article you provided in the setup process. Once a member of your group has their birthday, the bot will congratulate them to their birthday at the time you provided and updates the article.

In order to set the bot up, you need to fill out the hardcode_values.py file. I expect you to be able to fill out TELEGRAM_TOKEN, GROUP_ID and TIME by yourself. I suggest to put the public name of your group in GROUP_NAME. That string is used to point non members of the previous chat id to the correct group. It is only used in a text message, so you can write whatever you want though.

The three values left require the setup I spoke about earlier. In order to obtain a Telegraph token, you need to create an account with their API. Check out the documentation at https://telegra.ph/api. As of writing this ReadMe, the correct URL to create a new account is https://api.telegra.ph/createAccount?short_name=birthday_bot&author_name=Birthday%20Bot. You are greeted with a JSON response. Plug the access_token into TELEGRAPH_TOKEN. Now I suggest to just click on auth_url. If you do this, you are logged into telegra.ph. Now you can create an article. Once you finished this, take the part after the domain and paste it into ARTICLE_ID. Now you can change the TELEGRAPH_TITLE as well, otherwise whatever you put as the title will be overriden once the bot has a birthday to put into the article.

That is it. Install the requirements, start it, enjoy it. All strings are in strings.py, you can just translate them in there. I already did this for German, so when you want to use the bot in this language, just delete string.py and rename string_de.py to, you guessed it, string.py.

