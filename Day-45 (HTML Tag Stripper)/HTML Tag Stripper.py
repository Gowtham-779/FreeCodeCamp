def strip_tags(html):
    result = ""
    inside_tag = False
    for char in html:
        if char == '<':
            inside_tag = True
        elif char == '>':
            inside_tag = False
        elif not inside_tag:
            result += char
    return result
