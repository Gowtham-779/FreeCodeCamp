def battle(our_team, opponent):
    our_wins = 0
    opponent_wins = 0
    for our_word, opp_word in zip(our_team.split(), opponent.split()):
        our_value = sum(
            (ord(c.lower()) - ord('a') + 1) * (2 if c.isupper() else 1)
            for c in our_word
        )
        opp_value = sum(
            (ord(c.lower()) - ord('a') + 1) * (2 if c.isupper() else 1)
            for c in opp_word
        )
        if our_value > opp_value:
            our_wins += 1
        elif our_value < opp_value:
            opponent_wins += 1
    if our_wins > opponent_wins:
        return "We win"
    if our_wins < opponent_wins:
        return "We lose"
    return "Draw"