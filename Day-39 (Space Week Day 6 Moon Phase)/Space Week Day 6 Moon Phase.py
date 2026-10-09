from datetime import date
def moon_phase(date_string):
    reference = date(2000, 1, 6)
    given_date = date.fromisoformat(date_string)
    days_passed = (given_date - reference).days
    day = (days_passed % 28) + 1
    if day <= 7:
        return "New"
    elif day <= 14:
        return "Waxing"
    elif day <= 21:
        return "Full"
    else:
        return "Waning"