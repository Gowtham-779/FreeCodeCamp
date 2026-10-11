def hex_to_decimal(hex):
    total = 0
    for char in hex:
        if char.isdigit():
            value = int(char)
        else:
            value = ord(char) - ord('A') + 10
        total = total * 16 + value
    return totalx