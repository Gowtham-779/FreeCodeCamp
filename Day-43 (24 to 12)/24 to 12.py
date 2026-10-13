def to_12(time):
    hour = int(time[:2])
    minutes = time[2:]
    if hour == 0:
        hour = 12
        period = "AM"
    elif hour < 12:
        period = "AM"
    elif hour == 12:
        period = "PM"
    else:
        hour -= 12
        period = "PM"
    return f"{hour}:{minutes} {period}"