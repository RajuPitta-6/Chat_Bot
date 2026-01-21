
import re

class TextPreprocessor:
    @staticmethod
    def clean_text(texts):
        clean_text = []
        for text in texts:
            text = text.lower()
            text = re.sub(r"[^a-z\s]", " ", text)
            text = re.sub(r"\s+", " ", text).strip()
            clean_text.append(text)
        return clean_text

