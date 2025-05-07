from main import aiDecision

def test_main():
    print("Test 1: Pre-flop, strong hand (AA), neutral emotion: Expect raise or all-in")
    nums = [14, 14, 0, 0, 0, 0, 0, 0, 0]  # AI: AA, rest unknown
    suits = ['Spades', 'Hearts', "", "", "", "", "", "", ""]  
    print("Decision:", main(nums, suits, emotion=0, weight=0.1))  # Expect raise or all-in

    print("\nTest 2: Pre-flop, weak hand (7-2 offsuit), neutral emotion: Expect call or fold")
    nums = [7, 2, 0, 0, 0, 0, 0, 0, 0]
    suits = ['Spades', 'Diamonds', "", "", "", "", "", "", ""]
    print("Decision:", main(nums, suits, emotion=0, weight=0.1))  # Expect call or fold

    print("\nTest 3: Flop visible, one pair, positive emotion: Emotion may lead to raise")
    nums = [9, 2, 0, 0, 9, 5, 3, 0, 0]  # AI pairs with flop
    suits = ['Clubs', 'Hearts', "", "", 'Hearts', 'Diamonds', 'Spades', "", ""]
    print("Decision:", main(nums, suits, emotion=0.5, weight=0.2))  # Emotion may lead to raise

    print("\nTest 4: Turn visible, strong draw, negative emotion: May fold due to emotion")
    nums = [11, 12, 0, 0, 10, 9, 2, 0, 0]  # Strong straight draw
    suits = ['Spades', 'Spades', "", "", 'Spades', 'Spades', "", "", ""]
    print("Decision:", main(nums, suits, emotion=-0.7, weight=0.3))  # May fold due to emotion

    print("\nTest 5: River complete, flush, neutral emotion: Expect raise or all-in")
    nums = [4, 9, 0, 0, 6, 7, 8, 10, 2]  # AI has a flush
    suits = ['Hearts', 'Hearts', "", "", 'Hearts', 'Hearts', 'Diamonds', 'Spades', 'Hearts']
    print("Decision:", main(nums, suits, emotion=0, weight=0.1))  # Expect raise or all-in

test_main()
