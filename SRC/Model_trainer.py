from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
import joblib

from Preprocessing import TextPreprocessor
from Config import  MODEL_PATH, MAX_FEATURES, VECTORIZER_PATH


class ModelTrainer:
    def train(self, x, y):
        x_clean = TextPreprocessor.clean_text(x)

        vectorizer = TfidfVectorizer(ngram_range=(1, 2),max_df=0.9,
                                     max_features=MAX_FEATURES,
                                     min_df=2,sublinear_tf=True)
        X_vec = vectorizer.fit_transform(x_clean)

        model = LinearSVC(C=2.0, class_weight='balanced',)
        model.fit(X_vec, y)

        joblib.dump(model, MODEL_PATH)
        joblib.dump(vectorizer, VECTORIZER_PATH)


        print("Model training is complete")
