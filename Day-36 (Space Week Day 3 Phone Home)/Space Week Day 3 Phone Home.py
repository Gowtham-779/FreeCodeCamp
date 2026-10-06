def send_message(route):
    total_distance = sum(route)
    travel_time = total_distance / 300000
    satellites = len(route) - 1
    delay = satellites * 0.5
    return round(travel_time + delay, 4)