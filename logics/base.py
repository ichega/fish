import re
import random

fucks = open('names.txt', 'r').read().split()
aliases = [
    "рыба", "Рыба", "топленая", "Топленая", "fish", "Fish",
    "РЫБА", "ТОПЛЕНАЯ", "FISH",

]

def rand_fucks():
    return fucks[random.randint(0, len(fucks)-1)]



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

def jekakill(user_id, message):
    text = ""



    if " " in message:
        words = str(message).split()
    else:
        words = [message]

    try:
        words = str(message).split()
        if words[0] in aliases:
            if words[1] in ["агр", "агрись", "жекакил"]:
                return True, f"Я сама не могу, но ты скажи жеке, что он - '{fucks[random.randint(0, len(fucks)-1)]}'"

    except:
        return False, ""
    return False, ""

def writetoivan(user_id, message):
    if message == "рыба напиши ване":
        text = f"@id362326531 (Иван), я знаю слово '{fucks[random.randint(0, len(fucks)-1)]}', а ты что?"




        return True, text
    else:
        return False, ""

def check(id, message, question, answer):
    if message == question:
        return True, answer
    return False, ""


def check_fuck(id, message):
    text = message.split()
    found = False
    for word in text:
        if word in fucks:
            found = True
            break
    answers = [
        'Охуел?! рыбья залупонь..',
        f'Иди говна поешь {rand_fucks()}',
        'Твою мать топила, сученок',
        f'Рыба всплыла и по {rand_fucks()} дала тебе',
        'В тихом омуте бомжи топятся..а прости, это ты',
    ]
    if found:
        return True, answers[random.randint(0, len(answers)-1)]
    else:
        return False, ""




def hard_print(message):
    return True, message




