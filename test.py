from pokerface import main

# Test Case 1: High Probability, Neutral Emotion
cardNums_1 = [14, 12, 0, 0, 10, 11, 12, 13, 14]  # AI: Ace, Queen; Opponent: UNKNOWN; Community: 10, Jack, Queen, King, Ace
cardSuites_1 = ['Hearts', 'Clubs', '', '', 'Clubs', 'Hearts', 'Diamonds', 'Spades', 'Diamonds']  # Suits for AI, opponent (unknown), and community cards

emotion_1 = 0  # Neutral emotion
weight_1 = 0  # Emotion weight does not affect

print("Test Case 1 - High Probability, Neutral Emotion:")
print(main(cardNums_1, cardSuites_1))  # Expected outcome: 100 (All-in, high confidence)

# Test Case 2: Low Probability, Neutral Emotion
cardNums_2 = [2, 3, 0, 0, 9, 10, 11, 12, 13]  # AI: 2, 3; Opponent: UNKNOWN; Community: 9, 10, Jack, Queen, King
cardSuites_2 = ['Spades', 'Diamonds', '', '', 'Spades', 'Diamonds', 'Clubs', 'Hearts', 'Spades']  # Suits for AI, opponent (unknown), and community cards

emotion_2 = 0  # Neutral emotion
weight_2 = 0  # Emotion weight does not affect

print("Test Case 2 - Low Probability, Neutral Emotion:")
print(main(cardNums_2, cardSuites_2))  # Expected outcome: -1 (Fold)

# Test Case 3: Positive Emotion
cardNums_3 = [10, 11, 0, 0, 14, 9, 8, 11, 12]  # AI: 10, Jack; Opponent: UNKNOWN; Community: Ace, Jack, Queen, King, 10
cardSuites_3 = ['Hearts', 'Clubs', '', '', 'Clubs', 'Hearts', 'Spades', 'Diamonds', 'Clubs']  # Suits for AI, opponent (unknown), and community cards

emotion_3 = 0.7  # Positive emotion (AI is confident)
weight_3 = 0.5  # Emotion weight

print("Test Case 3 - Positive Emotion Affects Decision:")
print(main(cardNums_3, cardSuites_3))  # Expected outcome: 100 (All-in due to positive emotion)

# Test Case 4: Negative Emotion (Less Confident)
cardNums_4 = [2, 3, 0, 0, 9, 10, 11, 12, 13]  # AI: 2, 3; Opponent: UNKNOWN; Community: 9, 10, Jack, Queen, King
cardSuites_4 = ['Spades', 'Diamonds', '', '', 'Spades', 'Diamonds', 'Clubs', 'Hearts', 'Clubs']  # Suits for AI, opponent (unknown), and community cards

emotion_4 = -0.7  # Negative emotion (AI is sad)
weight_4 = 0.5  # Emotion weight

print("Test Case 4 - Negative Emotion Affects Decision:")
print(main(cardNums_4, cardSuites_4))  # Expected outcome: -1 (Fold due to negative emotion)

# Test Case 5: Neutral Emotion (Unchanged Decision)
cardNums_5 = [7, 8, 0, 0, 9, 10, 11, 12, 13]  # AI: 7, 8; Opponent: UNKNOWN; Community: 9, 10, Jack, Queen, King
cardSuites_5 = ['Spades', 'Hearts', '', '', 'Spades', 'Hearts', 'Diamonds', 'Clubs', 'Spades']  # Suits for AI, opponent (unknown), and community cards

emotion_5 = 0  # Neutral emotion
weight_5 = 0  # Emotion weight does not affect

print("Test Case 5 - Neutral Emotion (Unchanged Decision):")
print(main(cardNums_5, cardSuites_5))  # Expected outcome: Likely to call or raise, based on the probability

# Test Case 6: Tie Scenario (Edge Case)
cardNums_6 = [10, 12, 0, 0, 13, 14, 11, 12, 10]  # AI: 10, Jack; Opponent: UNKNOWN; Community: Ace, Jack, Queen, King, 10
cardSuites_6 = ['Spades', 'Clubs', '', '', 'Spades', 'Clubs', 'Hearts', 'Diamonds', 'Clubs']  # Suits for AI, opponent (unknown), and community cards

emotion_6 = 0  # Neutral emotion
weight_6 = 0  # Emotion weight does not affect

print("Test Case 6 - Tie Scenario:")
print(main(cardNums_6, cardSuites_6))  # Expected outcome: Ties or some neutral decision based on the tie logic in `monteCarlo`
