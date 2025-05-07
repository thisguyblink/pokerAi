
# Have this this be a list of strings and I can change it into numbers later, also J = 11, Q =12 ....
# If there is no community card for the slot then put NONE
# Cardnumbers = [aiCard1, aiCard2, community1, community2, community3, community4, communtiy5, aichips, opponentchips]

# Have this be string to for the suits
# Cardsuites = [aiCard1, aiCard2, community1, community2, community3, community4, communtiy5]


# list values: ai1, ai2, opp1, opp2, com1, com2, com3, com4, com5 for checking winner
import random
from evaluate import checkWinner
from emotionReader import read_image

# val == 1 ALL IN 
# val > .5 RAISE PROPORTIONALLY 
# val < .5 and > 0  CALL PROPORTIONALLY
# val == 0, call if no raise
# val < 0 FOLD

def decision(prob):
    # All in 
    if prob > .95:
        return 1
    # Raise 
    if prob < .95 and prob >.75:
        return prob
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
        # print(f'Simulation #{i}')
        # print(f'Card numbers: {nums}')
        # print(f'Card Suites: {suits}')
        val = simulate(nums, suits)
        # print(f'Simulation Value: {val}')
        if  val == 1:
            aiWins += 1
        elif val == .5:
            ties += 1
        else:
            oppWins += 1
    print(f'Ai Wins: {aiWins}')
    print(f'Ties: {ties}')
    print(f'Human Wins: {oppWins}')
    return aiWins / sims

# list values: ai1, ai2, opp1, opp2, com1, com2, com3, com4, com5 for checking winner

# Kinda work but keeping just incase 
def simulate2(nums, suits):
    ranks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    types = ['Spade', 'Heart', 'Diamond', 'Club']
    allNums = [0] * 9
    allSuits = ["-"] * 9
    for i in range(9):
        if nums[i] != 0:
            allNums[i] = nums[i]
        else: 
            allNums[i] = random.choice(ranks)
        if suits[i] != "":
            allSuits[i] = suits[i]
        else:
            allSuits[i] = random.choice(types)
    return checkWinner(allNums, allSuits)

# Decided to do second version since the first one isn't generating new cards sometimes???
# Edit: This one works so I'm keeping it :)
def simulate(nums, suits):

    deck = [(num, suit) for num in range(2, 15) for suit in ['Spade', 'Heart', 'Diamond', 'Club']]
    
    known_cards = [(nums[i], suits[i]) for i in range(9) if nums[i] != 0 and suits[i] != ""]

    deck = [card for card in deck if card not in known_cards]
    random.shuffle(deck)

    allNums = nums[:]
    allSuits = suits[:]

    for i in range(9):
        if allNums[i] == 0 or allSuits[i] == "":
            rand_card = deck.pop()
            allNums[i], allSuits[i] = rand_card

    return checkWinner(allNums, allSuits)

# emotion and weight for emotion can be set during the api call in the flask server
def aiDecision(cardNums, cardSuites, emotion, weight):
    unweightedProb = monteCarlo(cardNums, cardSuites, 100)
    print(f'Unweighted Probability: {unweightedProb}' )
    weightedProb = addEmotion(unweightedProb, emotion, weight)
    print(f'Weighted Probability: {weightedProb}')
    return decision(weightedProb)

def response(cardNums, cardSuites, weight, img):
    emotion, _ = read_image(img)
    aiDecision(cardNums, cardSuites, emotion, weight)

  