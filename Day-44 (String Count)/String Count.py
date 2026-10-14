def count(text, parameter):
    total = 0
    for i in range(len(text) - len(parameter) + 1):
        if text[i:i + len(parameter)] == parameter:
            total += 1
    return total