def is_pangram(sentence, letters):
    sentence = sentence.lower()
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for char in sentence:
        if char in alpha and char not in letters:
            return False
    for char in letters:
        if char not in sentence:
            return False

    return True