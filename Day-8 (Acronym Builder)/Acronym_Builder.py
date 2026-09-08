def build_acronym(s):
    words = s.split()
    ignore = ["a","for","an","and","by","of"]
    acronym = ""
    for i in range(len(words)):
        word = words[i].lower()
        if i == 0:
            acronym += word[0].upper()
        elif word in ignore:
            continue
        else:
            acronym += word[0].upper()
    return acronym