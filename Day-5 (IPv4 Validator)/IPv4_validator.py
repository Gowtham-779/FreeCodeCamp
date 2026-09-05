def is_valid_ipv4(ipv4):
    parts = ipv4.split(".")
    if len(parts) != 4:
        return False
    for i in parts:
        if not i.isdigit():
            return False
        if len(i)>1 and i[0]== '0':
            return False
        if int(i)>255:
            return False

    return True