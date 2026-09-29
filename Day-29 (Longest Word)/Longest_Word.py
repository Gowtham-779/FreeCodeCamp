def get_longest_word(sentence):
    words = sentence.replace(".", " ").split()
    high = ""
    for word in words:
        if len(word) > len(high):
            high = word
    return high

