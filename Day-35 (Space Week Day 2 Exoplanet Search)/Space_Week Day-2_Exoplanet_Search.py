def has_exoplanet(readings):
    result = []
    for ch in readings:
        if ch.isdigit():
            result.append(int(ch))
        else:
            result.append(ord(ch) - ord('A') + 10)
    average = sum(result) / len(result)
    for r in result:
        if r <= average * 0.8:
            return True
    return False