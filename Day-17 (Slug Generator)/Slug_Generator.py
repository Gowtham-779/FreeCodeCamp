def generate_slug(text):
    result = ""
    space = False
    for char in text:
        if char.isalnum():
            result += char.lower()
            space = False
        elif char == " ":
            if result and not space:
                result +="%20"
                space = True
    if result.endswith("%20"):
        result = result[:-3]
    return result