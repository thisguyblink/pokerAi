# Poker AI Bot

This project implements a Poker AI bot for playing Texas Hold'em using a Monte Carlo simulation to evaluate the bot's hand against an opponent's hand. The bot makes decisions (fold, call, raise, or all-in) based on the probability of winning a hand.

The AI is integrated with a Flask backend to handle the computation requests. This is designed to be part of a Unity 3D Texas Hold'em game, where it can be used for simulating poker games in real-time.

## Features

- **Monte Carlo Simulation**: Simulates multiple poker game scenarios to estimate the probability of winning a hand.
- **Emotion-Based Adjustments**: The AI decision-making process takes into account the player's emotional state, allowing the AI to make aggressive or conservative plays.
- **Poker Hand Evaluation**: Includes checking for different poker hands (Royal Flush, Straight, Pair, etc.) to determine the winner.
- **API Integration**: The Flask API can accept JSON requests with card information and return the AI's decision.

## Files

### `main.py`

This is the main logic file that contains:

- The AI decision-making process using the `decision` function.
- The Monte Carlo simulation (`monteCarlo` and `simulate`) for evaluating the AI's chance of winning.
- The function `addEmotion` to modify the AI's decision based on emotional input.
- The Flask routes to handle API requests (`/compute` and `/test`).

### `evaluate.py`

Contains the poker hand evaluation functions to determine the winner between two players (AI vs. opponent).

- **Functions**:
  - `checkWinner`: Evaluates the hands of both players and determines the winner.
  - `checkAll`: Checks for all possible poker hands, such as Royal Flush, Straight, Full House, etc.
  - Other specific functions for each hand (e.g., `royalFlush`, `straightFlush`, `fourOfAKind`, etc.).

### `score.py`

The `score` function calculates the score of the player's hand based on the cards held. It provides an evaluation of the hand strength, considering the hand type (pair, flush, straight, etc.) and ranks the cards accordingly.

### `pokerface.py`

Contains the logic to simulate the poker game and test various scenarios. It uses the decision-making logic and simulates real poker hands.

### `tests.py`

Includes test cases for the AI's decision-making, simulating different poker hands, and checking how the AI responds with various emotional weights.

## API Usage

### Endpoints

POST http://localhost:8080/compute

{
  "cards": [14, 14, 0, 0, 0, 0, 0, 0, 0],
  "suits": ["Spades", "Hearts", "", "", "", "", "", "", ""],
  "emotion": 0.5,
  "weight": 0.2
}

{
  "value": 0.9
}

## Where value indicates the AI's decision:

1: All-In

> 0.5: Raise

> 0 and < 0.5: Call

0: Call if no raise

< 0: Fold

#### `GET /test`

Returns a test message to confirm the server is running.
GET http://localhost:8080/test
Example: 

{
  "message": "Hello from Flask!"
}


### Running the Poject

1) Clone the Repo and go Into the poker=ai folder
        git clone https://github.com/yourusername/poker-ai.git
        cd poker-ai
2) Install Dependancies
        pip install -r requirements.txt
3) Run the Flask Server
    python server.py

### The server will be running at: http://localhost:8080
-- To change the 