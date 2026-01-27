from SRC.predict import ChatBot


# Single shared chatbot instance for the whole Streamlit session.
_chatbot = ChatBot()


def get_response(user_message: str) -> str:
    """
    Thin backend wrapper for the chatbot.

    The UI layer (Streamlit app) should only call this function,
    so all NLP/model logic stays inside the backend.
    """
    return _chatbot.predict(user_message)

