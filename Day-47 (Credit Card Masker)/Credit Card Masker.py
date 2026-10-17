def mask(card):
    result = ""
    count = 0
    for ch in card:
        if ch.isdigit():
            if count < 12:
                result += "*"
            else:
                result += ch
            count += 1
        else:
            result += ch
    return result
