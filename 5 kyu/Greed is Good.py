from collections import Counter

def score(dice):
    counts = Counter(dice)
    total_score = 0
    
    triplet_scores = {1: 1000, 6: 600, 5: 500, 4: 400, 3: 300, 2: 200}
    single_scores = {1: 100, 5: 50}
    
    for num, count in counts.items():
        if count >= 3:
            total_score += triplet_scores.get(num, 0)
            count -= 3 

        if num in single_scores:
            total_score += single_scores[num] * count
    
    return total_score
