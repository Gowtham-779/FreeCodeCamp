import math
def goldilocks_zone(mass):
    l = mass**3.5
    d = math.sqrt(l)
    start = 0.95*d
    end = 1.37*d
    return [round(start,2),round(end,2)]