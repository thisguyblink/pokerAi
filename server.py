from main import response
from flask import Flask, request, jsonify
from flask_cors import CORS
from emotionReader import read_image
import json

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes and origins

@app.route('/test', methods=['GET'])
def hello():
    return jsonify({"message": "Hello from Flask!"})

@app.route('/compute', methods=['POST'])
def compute():
    print(request.form)
    
    # Access the JSON data for cards, suits, and ratio
    cards = request.form.get("cards")
    suits = request.form.get("suits")
    ratio = request.form.get("ratio")

    # Print the raw data
    print(cards)
    print(suits)

    # Convert the JSON strings to Python data (parse the items list directly)
    cards_dict = json.loads(cards)
    suits_dict = json.loads(suits)

    # Extract the 'items' lists
    cards_list = cards_dict.get("items", [])
    suits_list = suits_dict.get("items", [])

    # Print the extracted lists
    print(cards_list)
    print(suits_list)

    # The image data is a binary file uploaded as 'image'
    img = request.files.get("image")

    # Make sure to check if the image is received properly
    if img:
        print("Image received.")
        # Call your response function, which should handle the image
        emotion, _ = read_image(img)  # Pass the file object to read_image
        print(f"Emotion detected: {emotion}")
    
    # Call the decision-making logic
    return jsonify({"value": response(cards_list, suits_list, ratio, img)})



if __name__ == '__main__':
    app.run(port=8080)
