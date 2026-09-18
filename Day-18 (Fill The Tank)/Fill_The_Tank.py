def cost_to_fill(tank_size, fuel_level, price_per_gallon):
    fuel_needed = tank_size - fuel_level
    cost = fuel_needed*price_per_gallon
    return f"${cost:.2f}"