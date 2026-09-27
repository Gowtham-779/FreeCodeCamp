def is_spam(number):
    country = number[1:number.index("(")-1]
    start = number.index("(")+1
    area = number[start:start+3]
    local_start = number.index(")")+2
    local = number[local_start:].replace("-","")
    if len(country) > 2 or not country.startswith("0"):
        return True
    if int(area) > 900 or int(area) < 200:
        return True
    first_three_sum = sum(int(digit) for digit in local[:3])
    if str(first_three_sum) in local[3:]:
        return True
    digits = country + area + local
    for i in range(len(digits) - 3):
        if digits[i] == digits[i + 1] == digits[i + 2] == digits[i + 3]:
            return True
    return False