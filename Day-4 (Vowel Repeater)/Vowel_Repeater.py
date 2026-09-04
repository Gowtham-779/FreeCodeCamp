def repeat_vowels(string):
    vowels = "aeiouAEIOU"
    result = ""
    count = 0
    for char in string:
        if char in vowels:
            count += 1
            result += char
            result += char.lower()*(count-1)
        else:
            result += char
    return result