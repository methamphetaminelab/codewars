def score_hand(cards):
    acesCount = 0
    score = 0
    print(cards)
    
    for card in cards:
        print(card)
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

    while score > 21 and acesCount <= 0:
        score = score_hand(cards[:-1])
        
    return score

print(score_hand(['4','5','6']))
print(score_hand(['K','J','Q']))
print(score_hand(['A', '2', 'A', '9', '9']))