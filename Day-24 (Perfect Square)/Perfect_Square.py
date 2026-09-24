def is_perfect_square(n):
    if n <0:
        return False
    num = int(n**0.5)
    return num*num == n