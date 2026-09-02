def rgb_to_hex(rgb):
    rgb = rgb.replace('rgb(','').replace(')','')
    temp = rgb.split(',')
    dic = {
        10:'a',
        11:'b',
        12:'c',
        13:'d',
        14:'e',
        15:'f'
    }
    rgb='#'
    for i in range(3):
        x = int(temp[i])
        q= x//16
        r= x%16
        if q>=10:
            rgb+=dic[q]
        else:
            rgb+=str(q)
        if r>=10:
            rgb+=dic[r]
        else:
            rgb+=str(r)
    return rgb