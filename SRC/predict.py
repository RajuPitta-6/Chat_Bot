import os
import sys

# Ensure this directory (SRC) is on sys.path so local imports work
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.append(CURRENT_DIR)

from Config import MODEL_PATH, VECTORIZER_PATH, DATA_PATH
from Preprocessing import TextPreprocessor
import joblib
import numpy as np



class Tagpredictor:
    def __init__(self, threshold=0.1):
        self.model = joblib.load(MODEL_PATH)
        self.vectorizer = joblib.load(VECTORIZER_PATH)
        self.threshold = threshold
    def predictor(self, message):
        clean = TextPreprocessor.clean_text([message])
        vect = self.vectorizer.transform(clean)
        raw_socre = self.model.decision_function(vect)[0]
        sorted_score= np.sort(raw_socre)
        confidence = sorted_score[-1] - sorted_score[-2]


        if confidence >= self.threshold:
            # Take the single predicted label as a plain string
            tag = self.model.predict(vect)[0]
            return tag
        else:
            # Low confidence: use fallback intent
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