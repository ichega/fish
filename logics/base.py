import re
import random




def hello(user_id, text):
    text = ""
    welcomes = [
        "рыба", "Рыба", "топленая", "Топленая", "fish", "Fish"
    ]
    WELCOMES = [
        "РЫБА", "ТОПЛЕНАЯ", "FISH"
    ]
    words = str(text).split()
    found = False
    for word in words:
        if word in welcomes:
            found = True
            text = f"{[]}"
            return found, text

    return found, text



