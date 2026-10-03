def check_strength(password):
    score =0
    if len(password) >= 8:
        score +=1
    if any(c.isupper() for c in password) and any(c.islower() for c in password):
        score +=1
    if any(c.isdigit() for c in password):
        score +=1
    if any (c in "!@#$%^&*" for c in password):
        score +=1

    if score <2:
        return "weak"
    if score <= 3:
        return "medium"
    return "strong"