
# score from 10 to 90 
# 0 is the worst possible hand 
# 100 is the best possible hand

def score(card1S, card1N, card2S, card2N):
    score = 0 
    
    # J = 11, Q = 12, K = 13, A = 14
    low = [2, 3, 4, 5, 6]
    medium = [7, 8, 9, 10]
    high = [11, 12, 13, 14]  

    # same suit or same num score + 10 for flush for pair to start
    if card1S == card2S:
        score += 10
    if card1N == card2N:
        score += 10
    
    # high + 40
    if card1N in high:
        score += 40
    if card2N in high:
        score += 40
        
    medium + 25
    if card1N in medium:
        score += 25
    if card2N in medium:
        score += 25
        
    # low + 10
    if card1N in low:
        score += 10
    if card2N in low:
        score += 10
    
    # - 10 for both card being low 
    if card1N in low and card2N in low:
        score -= 10
    
    # + 10 for cards being next to each other for straight
    if card1N == card2N + 1 or card1N == card2N - 1:
        score += 10
    else: 
        score -= 10
    
    return score