def to_binary(decimal):
    res=0
    p=1
    while decimal!=0:
        rem=decimal%2
        res = res + (rem*p)
        p*=10
        decimal//=2
    return str(res)