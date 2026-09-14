def get_words(paragraph):
    words = paragraph.lower().replace(",", "").replace(".", "").replace("!", "").split()
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    sorted_words = sorted(frequency, key=frequency.get, reverse=True)

    return sorted_words[:3]