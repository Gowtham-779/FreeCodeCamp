def second_largest(arr):
    num = list(set(arr))
    num.sort()
    return num[-2]