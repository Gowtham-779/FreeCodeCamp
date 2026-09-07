def parse_roman_numeral(numeral):
    val = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
    }
    total=0
    for i in range(len(numeral)):
        c = val[numeral[i]]
        if i+1 < len(numeral):
            next = val[numeral[i+1]]
            if c < next:
                total -= c
            else:
                total += c
        else:
            total += c
    return total