def launch_fuel(payload):
    total_fuel = 0
    add_fuel = payload / 5
    while True:
        total_fuel += add_fuel
        if add_fuel < 1:
            break
        add_fuel = add_fuel / 5
    return round(total_fuel, 1)