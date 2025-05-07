
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

# list values: ai1, ai2, opp1, opp2, com1, com2, com3, com4, com5
def checkWinner(cardNums, cardSuites):

    aiNums = cardNums[0:2] + cardNums[4:]
    aiSuits = cardSuites[0:2] + cardSuites[4:]
    oppNums = cardNums[2:4] + cardNums[4:]
    oppSuits = cardSuites[2:4] + cardSuites[4:]
    aiRank = checkAll(aiNums, aiSuits)
    oppRank = checkAll(oppNums, oppSuits)
    # print(f'AI Rank: {aiRank}')
    # print(f'OPP Rank: {oppRank}')

    if aiRank > oppRank:
        return 1
    if aiRank == oppRank:
        return 0.5
    if aiRank < oppRank:
        return 0


def checkAll(nums, suites):
    # First check for the highest hand (from Royal Flush to One Pair)
    score = royalFlush(nums, suites)
    if score > 0:
        return score
    
    score = straightFlush(nums, suites)
    if score > 0:
        return score
    
    score = fourOfAKind(nums)
    if score > 0:
        return score
    
    score = fullHouse(nums)
    if score > 0:
        return score
    
    score = flush(suites)
    if score > 0:
        return score
    
    score = straight(nums)
    if score > 0:
        return score
    
    score = threeOfAKind(nums)
    if score > 0:
        return score
    
    score = twoPair(nums)
    if score > 0:
        return score
    
    score = onePair(nums)
    if score > 0:
        return score
    
    return 1  # If no hand is matched, return 1 for high card


def royalFlush(nums, suites):
    suit_counts = {}
    for i in range(len(suites)):
        suit = suites[i]
        if suit in suit_counts:
            suit_counts[suit].append(nums[i])
        else:
            suit_counts[suit] = [nums[i]]

    # Check for a flush (same suit)
    for suit, suited_nums in suit_counts.items():
        if len(suited_nums) >= 5:
            suited_nums = sorted(set(suited_nums))

            # Check for a royal flush (A, K, Q, J, 10)
            if suited_nums == (10, 11, 12, 13, 14):
                return 10  # Found royal flush
    return 0


def straightFlush(nums, suites):
    suit_counts = {}
    for i in range(len(suites)):
        suit = suites[i]
        if suit in suit_counts:
            suit_counts[suit].append(nums[i])
        else:
            suit_counts[suit] = [nums[i]]

    # Check for a flush (same suit)
    for suit, suited_nums in suit_counts.items():
        if len(suited_nums) >= 5:
            suited_nums = sorted(set(suited_nums))  # Remove duplicates and sort

            # Check for a straight flush
            for i in range(len(suited_nums) - 4):
                window = suited_nums[i:i + 5]
                if window[4] - window[0] == 4:  # Check for consecutive numbers
                    return 9  # Found straight flush
    return 0

def fourOfAKind(nums):
    fours = {}
    for num in nums:
        if num in fours:
            fours[num] += 1
        else:
            fours[num] = 1
        if fours[num] == 4:
            return 8
    return 0


def fullHouse(nums):
    counts = {}
    
    for num in nums:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    
    threes = False
    pair = False
    
    # Check for 3 of a kind and a pair
    for count in counts.values():
        if count == 3:
            threes = True
        elif count == 2:
            pair = True
    if threes and pair:
        return 7
    return 0

def flush(suites):
    counts = {}
    
    for suit in suites:
        if suit in counts:
            counts[suit] += 1
        else: 
            counts[suit] = 1
        if counts[suit] == 5:
            # print(f'The Suit: {suit} count is: {counts[suit]}')
            return 6
    return 0

def straight(nums):
    nums = list(set(nums))         
    nums.sort()

    for i in range(len(nums) - 4):
        window = nums[i:i+5]
        if window[4] - window[0] == 4 and len(window) == 5:
            return 5
    return 0

def threeOfAKind(nums):
    threes = {}
    for num in nums:
        if num in threes:
            threes[num] += 1
        else:
            threes[num] = 1
        if threes[num] == 3:
            return 4
    return 0

def twoPair(nums):
    pairs = {}
    for num in nums:
        if num in pairs:
            pairs[num] += 1
        else:
            pairs[num] = 1

    pair_count = 0
    for count in pairs.values():
        if count >= 2:
            pair_count += 1
    if pair_count == 2:
        return 3
    return 0

def onePair(nums):
    pairs = {}
    for num in nums:
        if num in pairs:
            return 2
        else: 
            pairs[num] = 1
    return 0









