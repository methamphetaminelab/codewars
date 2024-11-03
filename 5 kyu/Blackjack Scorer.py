def score_hand(cards):
    acesCount = 0
    score = 0
    
    for card in cards:
        if card in 'JQK':
            score += 10
        elif card == 'A':
            acesCount += 1
            score += 11
        else:
            score += int(card)

    while score > 21 and acesCount > 0:
        score -= 10
        acesCount -= 1

    return score