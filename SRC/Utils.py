
from Intent_loader import IntentLoader



class DatasetBuilder :
    def __init__(self,intent):
          self.intent = intent



    def build_dataset(self):

        X = []
        Y = []
        for intent in self.intent:
            tag = intent['tag']
            for pattern in intent['patterns']:
                X.append(pattern)
                Y.append(tag)

        return X, Y




