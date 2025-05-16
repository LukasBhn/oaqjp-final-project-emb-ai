"""
This module deploys the server for emotion detection.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Return a dictionary of emotion scores for provided text to analyze

    Returns:
        dict: Emotion scores
    """
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    score_anger = response["anger"]
    score_disgust = response["disgust"]
    score_fear = response["fear"]
    score_joy = response["joy"]
    score_sadness = response["sadness"]
    dominant_emotion = response["dominant_emotion"]

    if dominant_emotion is None:
        return "Invalid text! Please try again!"
    else:
        return f"For the given statement, the system response is 'anger': {score_anger}, \
        'disgust': {score_disgust}, 'fear': {score_fear}, 'joy': {score_joy} \
        and 'sadness': {score_sadness}. The dominant emotion is {dominant_emotion}."

@app.route("/")
def render_index_page():
    """
    This function initiates the rendering of the main application
    page over the Flask channel
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
