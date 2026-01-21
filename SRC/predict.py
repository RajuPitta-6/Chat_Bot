from Config import MODEL_PATH, VECTORIZER_PATH,DATA_PATH
from Preprocessing import TextPreprocessor
import joblib
import numpy as np



class Tagpredictor:
    def __init__(self, threshold=0.5, s_threshold=0.5):
        self.model = joblib.load(MODEL_PATH)
        self.vectorizer = joblib.load(VECTORIZER_PATH)
        self.threshold = threshold
        self.s_threshold = s_threshold
    def predictor(self, message):
        clean = TextPreprocessor.clean_text([message])
        vect = self.vectorizer.transform(clean)
        raw_socre = self.model.decision_function(vect)
        confidence = np.max(np.abs(raw_socre))


        if confidence >= self.threshold:
            tag =  self.model.predict(vect)

            return tag

        else:
            return "fallback"






from Respond_manager import RespondManager
class ChatBot:
    def __init__(self):
        self.predictor = Tagpredictor()
        self.responder = RespondManager()

    def predict(self,message):
        Tag  = self.predictor.predictor(message)
        responses = self.responder.responce(Tag)
        return responses