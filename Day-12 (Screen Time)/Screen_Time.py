def too_much_screen_time(hours):
    for i in hours:
        if i>=10:
            return True
    for i in range(len(hours)-2):
        if(hours[i]+hours[i+1]+hours[i+2])/3 >=8:
            return True
    if sum(hours)/7>=6:
        return True
    return False