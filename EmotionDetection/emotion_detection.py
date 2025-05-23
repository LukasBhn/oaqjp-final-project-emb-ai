import requests
import json

def emotion_detector(text_to_analyse):
    # Define the URL for the sentiment analysis API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header)

    status_code = response.status_code

    result = {}

    emotions = ["anger", "disgust", "fear", "joy", "sadness", "dominant_emotion"]

    if status_code == 400:
        for emotion in emotions:
            result[emotion] = None
        return result
    else: 
        formatted_response = json.loads(response.text)
        
        for emotion in emotions:
            if emotion == "dominant_emotion":
                dominant_emotion = max(result, key=result.get)
                result["dominant_emotion"] = dominant_emotion
            else:
                result[emotion] = formatted_response["emotionPredictions"][0]["emotion"][emotion]

        return result
