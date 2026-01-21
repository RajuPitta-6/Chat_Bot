from  Config import DATA_PATH
from Intent_loader import IntentLoader
import random




class RespondManager:
    def __init__(self):
        load = IntentLoader(DATA_PATH)
        self.intents = load.load_intents()


    def responce(self, tag):
        for intent in self.intents:
            if intent['tag'] == tag:
                return random.choice(intent["responses"])

