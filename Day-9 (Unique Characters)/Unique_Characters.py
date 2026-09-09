def all_unique(s):
    result = []
    for char in s:
        if char in result:
            return False
        else:
            result.append(char)
    return True