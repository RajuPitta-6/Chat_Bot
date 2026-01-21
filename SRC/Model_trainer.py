from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
import joblib

from Preprocessing import TextPreprocessor
from Config import  MODEL_PATH, MAX_FEATURES, VECTORIZER_PATH


class ModelTrainer:
    def train(self, x, y):
        x_clean = TextPreprocessor.clean_text(x)

        vectorizer = TfidfVectorizer(max_features=MAX_FEATURES)
        X_vec = vectorizer.fit_transform(x_clean)

        model = LinearSVC()
        model.fit(X_vec, y)

        joblib.dump(model, MODEL_PATH)
        joblib.dump(vectorizer, VECTORIZER_PATH)


        print("Model training is complete")
