def speeding(speeds, limit):
    speed_count = 0
    total = 0
    for s in speeds:
        if s > limit:
            speed_count +=1
            total += (s - limit)
    if speed_count ==0:
        return [0,0]
    average = total/speed_count
    return [speed_count,average]