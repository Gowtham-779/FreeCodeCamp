def is_mirror(str1, str2):
    word_1 = ""
    word_2 = ""
    for char in str1:
        if char.isalpha():
            word_1 += char
    for char in str2:
        if char.isalpha():
            word_2 += char
    return word_1[::-1] == word_2