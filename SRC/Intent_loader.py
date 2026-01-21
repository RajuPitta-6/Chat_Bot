import json
import os
from  pathlib import Path

# path

class IntentLoader:
    def __init__(self, path):
       self.path = Path(path)
    def load_intents(self) -> dict:
        if not os.path.exists(self.path):
            raise FileNotFoundError(f'Intent file not found at {self.path}.')

        try:
            with open(self.path, 'r') as f:
                data = json.load(f)
                return data['intents']
        except FileNotFoundError:
            raise Exception ("intents.json is not found")


