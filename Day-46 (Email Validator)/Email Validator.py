def validate(email):
    if email.count("@") != 1:
        return False
    local, domain = email.split("@")
    if not local or not domain:
        return False
    if local[0] == "." or local[-1] == ".":
        return False
    if ".." in local or ".." in domain:
        return False
    for char in local:
        if not (char.isalnum() or char in "._-"):
            return False
    if "." not in domain:
        return False
    last_dot = domain.rfind(".")
    suffix = domain[last_dot + 1:]
    if len(suffix) < 2 or not suffix.isalpha():
        return False

    return True