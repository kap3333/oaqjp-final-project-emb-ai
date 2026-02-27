import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    response = requests.post(url, json = myobj,headers=headers)
    formatted_response = json.loads(response.text)

    emotions = formatted_response.get("emotionPredictions", [{}])[0].get("emotion", {})

    if emotions:
        dominant_emotion = max(emotions, key=emotions.get)
        result = emotions.copy()
        result['dominant_emotion'] = dominant_emotion
        return result
    else:
        return {
            'anger': 0.0,
            'disgust': 0.0,
            'fear': 0.0,
            'joy': 0.0,
            'sadness': 0.0,
            'dominant_emotion': None
        }
