def reverse_sentence(sentence):
    words = sentence.split()
    result = []
    for i in range(len(words)-1,-1,-1):
        result.append(words[i])

    return " ".join(result)