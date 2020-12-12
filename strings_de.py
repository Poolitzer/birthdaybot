from hardcode_values import GROUP_NAME


INTRO = "Hey du. Du willst also in unserer Gruppengeburtstagsliste sein? Topp. Bitte sende mir deinen Geburtstag. " \
        "Das Format ist TT.MM.YYYY"
BIRTHDAY_FAIL = "Herzlichen Glückwunsch. Dein Geburtstag ist ******..... Beep buup.... Converting input to birthday " \
                "failed.\n\nBitte sende dein Geburtstag in dem Format TT.MM.YYYY oder benutze /cancel"
SAY_NAME = "Sehr gut, ich habe dein Geburtstag gespeichert. Unter welchen Namen willst du in der Liste erscheinen?"
LINK = "Ich sehe, dass du einen Benutzernamen hast. Möchtest du den in unserer Liste mit deinem Namen verlinken?"
# we need the spaces after the dots because we combine it with Birthday_Show
LINK_APPROVED = "Okay, ich werde deinen Namen mit deinen Benutzernamen verlinken. "
LINK_DECLINED = "Okay, ich werde deinen Namen nicht verlinken. "
BIRTHDAY_SHOW = "Möchtest du, dass dein Geburtstag auf der Liste angezeigt wird?"
FINAL = "Okay, wunderbar. Ich habe deine Daten aufgenommen und den Telegraphartikel aktualisiert. " \
        "Herzlichen Glückwunsch"
GRATULATIONS = ["{0}, herzlichen Glückwunsch, du bist {1}!",
                "{0} hat Geburtstag, 🎉. {1} Jahre alt.", "JUNGS. {0} HAT GEBURTSTAG. {1} JAHRE!",
                "Herzlichen Glückwunsch zum Geburtstag, {0}, {1} Jahre schon, mann mann mann",
                "Wer erinnert sich noch dran, als er {1} Jahre alt war? Ihr könnt {0} fragen, die sind es heute \\o/",
                "{0} hat es geschafft heute Geburtstag zu haben und ist ganze {1} Jahre alt geworden.",
                "🎊🎉🥳🥳🥳🥳🙌🎉🎉🎉{0}🎊🎉🎊🎉🎊🎉🥳🙌🎉🥳🙌🎉🥳🙌🎉🥳🙌🎉{1}"]
FALLBACK = "Abgrebochen. ABGREBOCHEN. nix du auffer liste :("
NOT_IN_GROUP = f"Hey, du bist nicht in der coolen {GROUP_NAME} gruppe, daher werde ich dich nicht hinzufügen"
YES = "Ja"
NO = "Nein"
YEARS = "Jahre"
