import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, 'Data', 'intents.json')
model_dir = os.path.join(BASE_DIR, 'Model')
os.makedirs(model_dir, exist_ok=True)
model_path = os.path.join(model_dir, 'intent_model.pkl')
vectorizer_path = os.path.join(model_dir, 'intent_vectorizer.pkl')


INTENT_PATH = DATA_PATH
MODEL_PATH = model_path
VECTORIZER_PATH = vectorizer_path

MAX_FEATURES = 3000
