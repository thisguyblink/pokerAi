

# Have this this be a list of strings and I can change it into numbers later, also J = 11, Q =12 ....
# If there is no community card for the slot then put NONE
# Cardnumbers = [aiCard1, aiCard2, community1, community2, community3, community4, communtiy5, aichips, opponentchips]

# Have this be string to for the suits
# Cardsuites = [aiCard1, aiCard2, community1, community2, community3, community4, communtiy5]


# list values: ai1, ai2, opp1, opp2, com1, com2, com3, com4, com5 for checking winner
import random
from evaluate import checkWinner

def decision(prob):
    # All in 
    if prob > .95:
        return 100
    # Raise 
    if prob < .95 and prob >.75:
        return
    # Call Agressive
    if prob < .75 and prob > .50:
        return .25
    # Call Passive
    if prob < .5 and prob > .25:
        return 0
    # Fold 
    if prob < .25:
        return -1

# -1 is super happy and 1 is super sad
# might need to scale the input to match this
def addEmotion(probability, emotion, weight):
    return probability + (weight * emotion)


def monteCarlo(nums, suits, sims):
    aiWins = 0
    oppWins = 0
    ties = 0
    for i in range(sims):
        if simulate(nums) == 1:
            aiWins += 1
        if simulate(suits) == .5:
            ties += 1
        else:
            oppWins += 1
    return aiWins / sims

# list values: ai1, ai2, opp1, opp2, com1, com2, com3, com4, com5 for checking winner


def simulate(nums, suits):
    ranks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
    allNums = [0] * 9
    allSuits = ["-"] * 9
    for i in range(9):
        if nums[i] != 0:
            allNums[i] = nums[i]
        else: 
            allNums[i] = ranks[random.randint(0, 8)]
        if suits[i] == "":
            allSuits[i] == suits[i]
        else:
            allSuits == suits[random.randint(0, 3)]
    return checkWinner(allNums, allSuits)


# need to add emotion and weight as parameters but will use set numbers for now 
def main(cardNums, cardSuites):
    weight = .1
    emotion = .5
    unweightedProb = monteCarlo(cardNums, cardSuites, 100)
    weightedProb = addEmotion(unweightedProb, emotion, weight)
    return decision(weightedProb)

