def to_decimal(binary):
    l = len(binary)
    sum = 0
    for i in range(l):
        sum+= int(binary[l-1-i])*(2**i)
    return sum