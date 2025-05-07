from pokerface import main
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes and origins

@app.route('/test', methods=['GET'])
def hello():
    return jsonify({"message": "Hello from Flask!"})

@app.route('/compute', methods=['POST'])
def compute():
    data = request.json
    numsList = data["nums"]
    suitList = data["suits"]
    emotion = data["emotion"]
    weight = data["weight"]
    # need the data formatted like ai1, ai2, opp1, opp2, com1, com2, com3, com4, com5 for numbers and suits
    # also need emotion and weight for emotion
    # main(numsList, suitsList, emotion, weight)
    # val == 1 ALL IN 
    # val > .5 RAISE PROPORTIONALLY 
    # val < .5 and > 0  CALL PROPORTIONALLY
    # val == 0, call if no raise
    # val < 0 FOLD
    # These are the value it will return and what they mean 

    return jsonify({"value" : main(numsList, suitList, emotion, weight)})

if __name__ == '__main__':
    app.run(debug=True)
