def digits_or_letters(s):
    word =''
    num = ''
    for  i in s:
        if i.isalpha():
            word += i
        elif i.isdigit():
            num += i
    if len(word) >  len(num):
        return "letters"
    elif len(word) < len(num):
        return "digits"
    return "tie"