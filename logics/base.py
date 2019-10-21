import re
import random

fucks = open('names.txt', 'r').read().split()


def hello(user_id, message):
    text = ""
    welcomes = [
        "рыба", "Рыба", "топленая", "Топленая", "fish", "Fish"
    ]
    WELCOMES = [
        "РЫБА", "ТОПЛЕНАЯ", "FISH"
    ]

    print('text: ', message)
    if " " in message:
        words = str(message).split()
    else:
        words = [message]
    print(words)
    found = False
    for word in words:
        if word in welcomes:
            found = True
            answers = ["что?", "чо?", "я занята."]
            text = f"{answers[random.randint(0, len(answers)-1)]}"
            return found, text
        if word in WELCOMES:
            found = True
            if random.randint(0, 100) < 80:
                answers = [f"Что, {fucks[random.randint(0, len(fucks)-1)]}?"]
            else:
                answers = ["ЧО?", "ЙЙЙОУ", "Даун?", "Хромосому словил чтоле?"]

            text = f"{answers[random.randint(0, len(answers)-1)]}"
            return found, text

    return found, text

def fuck(user_id, message):
    text = ""
    welcomes = [
        "рыба", "Рыба", "топленая", "Топленая", "fish", "Fish"
    ]
    WELCOMES = [
        "РЫБА", "ТОПЛЕНАЯ", "FISH"
    ]

    print('text: ', message)
    if " " in message:
        words = str(message).split()
    else:
        words = [message]
    print(words)
    found = False
    for word in words:
        if word in welcomes:
            found = True
            answers = ["что?", "чо?", "я занята."]
            text = f"{answers[random.randint(0, len(answers)-1)]}"
            return found, text
        if word in WELCOMES:
            found = True
            answers = ["ЧО?", "ЙЙЙОУ", "Даун?", "Хромосому словил чтоле?"]
            text = f"{answers[random.randint(0, len(answers)-1)]}"
            return found, text

    return found, text



