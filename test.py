def contains_Im(text):
    if 'I am' in text:
        word = text.split("I am", 1)[1].split(" ")[1]
        return [True, word]

    if "I'm" in text:
        word = text.split("I'm", 1)[1].split(" ")[1]
        return [True, word]

    if "Im" in text:
        word = text.split("Im", 1)[1].split(" ")[1]
        return [True, word]

    if "im" in text:
        word = text.split("im", 1)[1].split(" ")[1]
        return [True, word]
    return [False, '']
